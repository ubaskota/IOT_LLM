import pandas as pd
import json
import sys

#This code is to convert a csv file to json file and that json
#file is used by openAi_finetune.py to train the model
def csv_to_json(input_csv, output_json):
    # Load the CSV file into a Pandas DataFrame
    df = pd.read_csv(input_csv)
    print("hello")
    # Convert DataFrame to list of dictionaries in the required format
    data = df.to_dict(orient='records')
    #print(data)
    # Save the data to a JSON file
    with open(output_json, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print("JSON data saved to...", output_json)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_csv_file> <output_json_file>")
        sys.exit(1)

    input_csv_file = sys.argv[1]
    output_json_file = sys.argv[2]

    csv_to_json(input_csv_file, output_json_file)
