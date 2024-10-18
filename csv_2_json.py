import csv
import json

def formatifier():
    # Load CSV file and convert to JSON
    csv_file = '/Users/christencampbell/PycharmProjects/Turmerik Task/clinical_trials_results.csv'  # Replace with your CSV file path
    json_file = 'output.json'

    # Read CSV file
    data = []
    with open(csv_file, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)

    # Write to JSON file
    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

    print(f"CSV file converted to {json_file}")

if __name__ == "__main__":
    formatifier()
