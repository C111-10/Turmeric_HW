# this script queries the patient condition data against
# the clinical trials. Uses spacy to analyse the first
# clinical trial at df.iat[1, 6] (the location of the
# eligibility criteria) then extracts the biomedical entity
# information. It the outputs the clinical_trials_results.csv
# as output.json.


import patient_cond_query
import criteriaBiomed_analysis
import csv_2_json

patient_cond_query.get_CTs()
criteriaBiomed_analysis.bioMedTerm_analysis()
csv_2_json.formatifier()

