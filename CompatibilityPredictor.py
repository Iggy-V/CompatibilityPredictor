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
    for i in teamList[0]['attributes']:
        attributeData[i] = []
    
    teamMembers = 0 
    for i in teamList:  
        teamMembers += 1
        for j in attributeData.keys():
            attributeData[j].append(i['attributes'].get(j, 0))
    
    weakpoints = 0
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
    normalizingConstant = len(applicant['attributes'])

    for i in applicant['attributes']:
        if applicant['attributes'][i] > attributeData[i][0]:

            compatibility += 0.5/(normalizingConstant)
        
        if applicant['attributes'][i] > 8:

            compatibility += 0.3/(normalizingConstant)

            if attributeData.get("weakpoints") == 0:
                compatibility += 0.2/(normalizingConstant)

            elif attributeData[i][-1] == 1:
                print("runs")
                compatibility += 0.2/(attributeData.get("weakpoints"))
        

        
    return {"name": applicant.get("name"), "score" : round(compatibility,3)}



def main():

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
            

            for i in data["applicants"]:
                scoredApplicants["Scored Applicants"].append(evaluateApplicant(teamData, i))


            f.close()
            with open(output_file, "w") as f:
                json.dump(scoredApplicants, f, indent=4)  # indent parameter for pretty formatting

        except:
            print("No such .json file in the directory")
            
if __name__ == "__main__":
    main()