# this file reads the patient conditions file and uses the clinical trials API to query
# for conditions present in the patient's csv and then saves a selection of the trial
# info. This is then saved to a csv titled clinical_trials_resuslts.csv

import pandas as pd
import requests

def get_CTs():
# Step 1: Load the data into a pandas DataFrame
    file = 'path/to/your/patient/conditions.csv'

    df = pd.read_csv(file)

    # Group the data by 'PATIENT' column and aggregate their conditions
    patient_conditions = df.groupby('PATIENT')['DESCRIPTION'].apply(list).reset_index()

    # Create an empty list to store trial results
    all_trials = []


    def query_clinical_trials_api(patient_id, condition):
        base_url = "https://clinicaltrials.gov/api/v2/studies"
        params = {
            "query.titles": condition,
            "query.term": "RECRUITING",
            "pageSize": 100
        }
    # Initialize an empty list to store the data
        data_list = []
        response = requests.get(base_url, params=params)
        # checks to see if the response was successful
        if response.status_code == 200:
            #data is returned as json format
            data = response.json()
            trials = data.get('studies', [])

            # this section
            if trials:
                print(f"Found {len(trials)} trials for {condition}:")
                for trial in trials:

                    nctId = trial['protocolSection']['identificationModule'].get('nctId', 'Unknown')
                    overallStatus = trial['protocolSection']['statusModule'].get('overallStatus', 'Unknown')
                    startDate = trial['protocolSection']['statusModule'].get('startDateStruct', {}).get('date',
                                                                                                        'Unknown Date')
                    conditions = ', '.join(
                        trial['protocolSection']['conditionsModule'].get('conditions', ['No conditions listed']))

                    studyType = trial['protocolSection']['designModule'].get('studyType', 'Unknown')
                    phases = ', '.join(trial['protocolSection']['designModule'].get('phases', ['Not Available']))
                    eligCri = trial['protocolSection']['eligibilityModule'].get('eligibilityCriteria')

                    # Append the trial info to the all_trials list
                    all_trials.append({
                        "NCT ID": nctId,
                        "Overall Status": overallStatus,
                        "Start Date": startDate,
                        "Conditions": conditions,
                        "Study Type": studyType,
                        "Phases": phases,
                        "Eligibility Criterion": eligCri,
                        'Patient ID': patient_id,
                        'Condition': condition
                    })
            else:
                print(f"No recruiting trials found for {condition}.")
        else:
            print(f"Error querying for {condition}: {response.status_code}")


    # Loop through each patient's conditions and query the API
    for index, row in patient_conditions.iterrows():
        patient_id = row['PATIENT']
        conditions = row['DESCRIPTION']

        print(f"Patient ID: {patient_id}, Conditions: {conditions}")

        # Query for each condition in the patient's list
        for condition in conditions:
            query_clinical_trials_api(patient_id, condition)

    # Step to save all the trials to a CSV file
    if all_trials:
        trials_df = pd.DataFrame(all_trials)  # Convert list of dicts to DataFrame
        trials_df.to_csv('clinical_trials_results.csv', index=False)  # Save to CSV
        print(f"All trial results saved to 'clinical_trials_results.csv'.")
    else:
        print("No trials found to save.")

if __name__ == "__main__":
    get_CTs()