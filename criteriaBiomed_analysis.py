# This is incomplete able to extract biomedical terms from the eligibility criteria in
# path/to/your/patient_cond_query/output/clinical_trial_results.csv
# for a single cell


import spacy
import scispacy
import pandas as pd

def bioMedTerm_analysis():
    # Load the small core model for biomedical data
    nlp = spacy.load("en_ner_bc5cdr_md")

    # Load the Named Entity Recognition (NER) model for biomedical terms
    ner_model = spacy.load("en_ner_bionlp13cg_md")

    file = "/path/to/your/clinical_trials_results.csv"
    df = pd.read_csv(file)

    # Dataframe is being used to isolate a cell of the csv for testing
    text = df.iat[1, 6]

    # Use the NER model to extract biomedical entities
#    doc = ner_model(text)
    doc = nlp(text)
    for ent in doc.ents:
        # We're interested in specific biomedical terms
        if ent.label_ in ['DISEASE', 'DISORDER', 'CONDITION']:
            print(ent.text)




if __name__ == "__main__":
    bioMedTerm_analysis()
