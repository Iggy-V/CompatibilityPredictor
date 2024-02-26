import json
import sys


def evaluateTeam(teamDict):
    attributeData = {}
    for i in teamDict[0]['attributes']:
        attributeData[i] = 0
    
    teamMembers = 0 
    for i in teamDict:
        teamMembers += 1
        for j in attributeData.keys():
            attributeData[j] += i['attributes'].get(j, 0)
        
    for i in attributeData.keys():
        attributeData[i] = attributeData[i]/teamMembers
    
    return attributeData

def evaluateApplicant(teamData, applicant):
    compatibility = 0
    for i in applicant['attributes']:
        if applicant['attributes'][i] > teamData[i]:
            compatibility += 0.25
        
    return {"name": applicant.get("name"), "score" : compatibility}



def main():

    if len(sys.argv) != 2:
        print("Usage: <applicant and team data file>")

    else:
        file = sys.argv[1]
        output_file = "output.json"

        f = open(file)
        data = json.load(f)
        
        scoredApplicants = {"Scored Applicants" : []}
        teamData = evaluateTeam(data["team"])
        

        for i in data["applicants"]:
            scoredApplicants["Scored Applicants"].append(evaluateApplicant(teamData, i))


        f.close()
        with open(output_file, "w") as f:
            json.dump(scoredApplicants, f, indent=4)  # indent parameter for pretty formatting


if __name__ == "__main__":
    main()