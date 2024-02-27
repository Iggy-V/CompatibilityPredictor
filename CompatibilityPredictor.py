"""
Compatibility Predictor is code that predicts how compatible are candidates to already existent team.
The compatibility is based on attributes of the workers and the team.

Author: Ignas Volcokas
"""
import json
import sys


def evaluateTeam(teamList):
    """
    Extraxts the data about the team from a given json file 'team' key.
    It gives the individual values for attributes, averages, and whether 
    the atribute is something that the team is missing.

    Parameters:
    teamList (list): contains dictonaries of the team membmers information

    Returns:
    attributeData (dict): dictionary that which contains the data attribute: [average, (whether it's lacking in the team 0/1)]
    """


    attributeData = {}
    # gets attributes based from the first member of the team
    for i in teamList[0]['attributes']:
        attributeData[i] = []
    
    teamMembers = 0 
    # creates a list of the attributes values that is going to be used for the average
    for i in teamList:  
        teamMembers += 1
        for j in attributeData.keys():
            attributeData[j].append(i['attributes'].get(j, 0))
    
    weakpoints = 0
    # checks if there are weakpoints (1-yes, 0-no) in the team and also counts the values
    for i in attributeData.keys():
        if max(attributeData[i]) < 8:
            weakpoints +=1
            attributeData[i] = [(sum(attributeData[i])/teamMembers), 1]
        else:
            attributeData[i] = [(sum(attributeData[i])/teamMembers), 0]
    
    attributeData["weakpoints"] = weakpoints
    return attributeData

def evaluateApplicant(attributeData, applicant):
    """
    Calculate the compatibility score of an individual applicant 

    Parameters:
    attributeData (dict): A dictionary of the data about the team's attributes.
    applicant (dict): dictonary of the applicants data.


    Returns:
    dict: of the "name" : name of the applicant and the "score" : score key-value pairs.
    """
    compatibility = 0
    normalizingConstant = len(applicant['attributes'])  #constant based on which compatibility is scaled

    for i in applicant['attributes']:
        #adds to compatibility if candidate attribute score higher than the average on the team 
        if applicant['attributes'][i] > attributeData[i][0]:

            compatibility += 0.5/(normalizingConstant)
        
        #adds to compatibility if candidate has extroaordinary ability in one of the fields
        if applicant['attributes'][i] > 8:

            compatibility += 0.3/(normalizingConstant)

            # checks if there are weakpoints if not just give all candidates 0.2 increase in compatibility
            if attributeData.get("weakpoints") == 0:
                compatibility += 0.2/(normalizingConstant)

            # if the candidate covers the weakpoint add to compatibility.
            elif attributeData[i][-1] == 1:
                compatibility += 0.2/(attributeData.get("weakpoints"))
        
        # if compatibility is above 1 or below 0 inform that the range of compatibilities is out of range, this indicates an error in prior code
        if compatibility > 1 or compatibility < 0:
            print("Inproperly scaled compatibility, must be in the range [0,1]")
            sys.exit()

        
    return {"name": applicant.get("name"), "score" : round(compatibility,3)}



def main():
    """
    Main function of the program.

    This function serves as the entry point to the program. It reads applicant and team data from a JSON file,
    evaluates each applicant based on team data, and generates an output JSON file containing scored applicants.

    Raises:
        FileNotFoundError: If the specified input JSON file is not found.
        ValueError: If the input file is not a valid JSON file.
        IOError: If there is an error while reading or writing files.

    Example:
        To run the program, specify the input JSON file as a command-line argument:
            python compatibilityPredictor.py input.json
    """
    if len(sys.argv) != 2:
        print("Usage: <applicant and team data file .json>")
    
    elif sys.argv[1].split(".")[-1] != "json":
        print("Input must be a .json file!")
    
    else:
        file = sys.argv[1]
        output_file = "output.json"
        
        try:
            f = open(file)
            data = json.load(f)

            scoredApplicants = {"Scored Applicants" : []}
            teamData = evaluateTeam(data["team"])
        
            #itterate through each candidate, append the data so that it can be nicely formated in json output
            for i in data["applicants"]:
                scoredApplicants["Scored Applicants"].append(evaluateApplicant(teamData, i))

            f.close()
            with open(output_file, "w") as f:
                json.dump(scoredApplicants, f, indent=4)

        except FileNotFoundError:
            print("No such .json file in the directory")

if __name__ == "__main__":
    main()