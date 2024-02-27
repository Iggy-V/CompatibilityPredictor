# Compatibility Predictor

Compatibility Predictor is a program designed to predict the compatibility of candidates with an existing team based on their attributes. The program evaluates individual applicants against the attributes of the team and generates compatibility scores for each applicant.

## Author

- **Ignas Volčokas**

## Features

- Predicts compatibility of candidates with an existing team.
- Evaluates candidates based on their attributes and team attributes.
- Generates compatibility scores for each applicant.

## How It Works

The program reads applicant and team data from a JSON file, evaluates each applicant based on team data, and generates an output JSON file containing scored applicants.

## Installation

- Clone the repository.
- Make sure you have Python (3.x) installed on your system.

## Usage

To use the Compatibility Predictor, follow these steps:

1. Prepare a JSON file containing data for both the team and applicants.
2. Run the program by executing the following command in your terminal:

```bash
python CompatibilityPredictor.py input.json
```

## Example

To run the program, specify the input JSON file as a command-line argument.
To run it with the example_input.json try the following command:
```bash
python CompatibilityPredictor.py example_input.json
```

## Future Work

While the current version of the Compatibility Predictor provides a basic assesment of compatibility a lot more can be done given more time and clearer goals. I had 
fun with the project so I thought I would brainstorm how could this be expanded. Here are my 3 suggestions.

1. **Machine Learning Integration**: Try to integrate machine learning algorithms to improve the predictions of compatibility. This could involve training the model on previous hires data and their performance, historic data of the team, etc. to better identify patterns.

2. **Dynamic Team Analysis**: Implement functionality to dynamically adjust compatibility based on the team composition and the goals set forth by the team. Or if there are two spaces open look for the pair of candidates that work best instead of singling out one individual.

3. **User Interface Enhancements**: Develop a user-friendly interface or dashboard to visualize compatibility scores. Make it easy for recruiters or HR team to extract relevant information with just one glance.

