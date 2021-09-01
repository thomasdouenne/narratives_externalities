# Authors:
- Thomas Douenne, University of Amsterdam, Roetersstraat 11, 1018 WB Amsterdam, Netherlands (email: t.r.g.r.douenne@uva.nl)
- Fanny Henriet, Paris School of Economics, CNRS
- Katheline Schubert, Paris School of Economics, Université paris 1 Panthéon-Sorbonne

# How to use this repo 'narratives_externalities'?
- Step 1: download data_qualtrics_pilot_narratives_raw.csv
- Step 2: run /preparation.py
- Step 3: explore answers to close ended questions with analysis_pilot.py
    and/or to close ended questions with analysis_open_questions_pilot.py

# List of files
data_qualtrics_pilot_narratives_raw.csv : this is the raw dataset directly downloaded from the Qualtrics survey

/analysis_open_questions_pilot.py : analyzes answers to open-ended questions
/analysis_pilot.py : produces descriptive statistics about survey respondents and survey responses
/caracteristiques_communes.py : depreciated, creates a .csv file that matches all French cities to their zip code
/LICENSE : GNU AFFERO GENERAL PUBLIC LICENSE
/preparation.py : from the raw dataset, produces a workable dataset with proper variable names and a set of additional useful variables
