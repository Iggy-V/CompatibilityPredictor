# Compatibility Predictor

Compatibility Predictor is a program designed to predict the compatibility of candidates with an existing team based on their attributes. The program evaluates individual applicants against the attributes of the team and generates compatibility scores for each applicant.

## Author

- **Ignas Volcokas**

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
python compatibilityPredictor.py input.json
```

## Example

To run the program, specify the input JSON file as a command-line argument.
To run it with the example_input.json try the following command:
```bash
python compatibilityPredictor.py example_input.json
```

