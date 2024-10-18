# Turmeric_HW
Clinical Trial Scraping & Patient Data Matching

Author: Christen Campbell

This project involves the extraction of clinical trial data from the ClinicalTrials.gov API
and the matching of patient conditions to relevant clinical trials. This project is not yet
robust or sophisticated.

I used only the "conditions.csv" file downloaded as part of the sample data sets from the
https://synthea.mitre.org/downloads resource, this is not due to a belief that the most
informative patient matching data resides here alone but more for prototype practice.


Requirements (for the ARM M1 Mac I have developed this on):
- Python Version: Python 3.8 (other versions may not be compatible with certain packages)

Key Python Libraries:
1. requests: For making HTTP requests to the ClinicalTrials.gov API.
   - Install via: pip install requests

2. pandas: For handling and organizing patient data in CSV format.
   - Install via: pip install pandas

3. Spacy: For general NLP processing, including entity linking. If you want to use entity
   linking functionality, you must install the relevant model in Spacy.
   - Install via: pip install spacy
   - Models for Spacy: https://spacy.io/models
(Spacy will be needed for advanced medical condition matching this library is not yet in
use functional as part of the script)

4. nmslib: To work efficiently with high-dimensional datasets such as medical or clinical
   trial data.
   - Install via:
     CFLAGS="-mavx -DWARN(a)=(a)" pip install nmslib

API Usage:
The project makes use of the ClinicalTrials.gov API v2 to retrieve information about
ongoing clinical trials that match specific conditions. Resources for the API's use:

https://clinicaltrials.gov/data-api/api
https://clinicaltrials.gov/data-api/about-api/search-areas#TitleSearch
https://clinicaltrials.gov/data-api/about-api/study-data-structure

version: 1.0.0
