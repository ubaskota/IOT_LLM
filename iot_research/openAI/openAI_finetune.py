import openai
import json
import sys
from openai import OpenAI

#This is file 2
#This code is to use the json file and finetune the model using gpt

# Set OpenAI API key
OPENAI_API_KEY = "key-here"      #Nwafor paid gpt-4.0
client = OpenAI(api_key=OPENAI_API_KEY)

def read_json(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

def prepare_training_data(data):
    training_data = []
    i = 0
    print("Feeding input .....")
    for item in data:
    # print("THis is item : ", item)
        #This is for other legacy models like babbage
        # training_data.append({
        #     'prompt': item['input_data'],
        #     'completion': item['label']
        # })
        # The attack type is determined from a predefined list "
        #     "including 'DoS', 'MIRAI', 'Recon', 'Web-Based', 'Spoofing', 'BenignTraffic', and 'Brute_Force'.
        # which should be either 'DoS' or non-Dos

        #This is where we assign the prompt. Change it accordingly
        training_data.append({
            "messages": [{"role": "system", "content": "This chatbot predicts the attack type based on the "
            "descriptive sentences provided by the user. Each descriptive sentence contains details of a network connection "
            "in numeric form, including 'IAT: The time difference with the previous packet', 'Min: minimum packet length in the flow', "
            "'Max: maximum packet length in the flow', 'Magnitue: square root of the sum of Average length of incoming and outgoing packets in the flow', "
            "'Tot sum : sum of packets in the flow', 'AVG: average packet length in the flow', 'Tot size : packet's length', "
            "'rst_count: number of packets with rst flag set in the flow', 'urg_count : number of packets with rst flag set in the flow ', "
            "'Header_Length : header length', 'label : the class label'. The attack type is determined from a predefined list "
            " which should be either 'DoS', or non-Dos"},
            {"role" : "user", "content": item['input_data']},
            {"role" : "assistant", "content" : item['label']}
            ]
        })
        i += 1
        if i % 1000 == 0:
            print("So far {} rows training completed! ".format(i))
    return training_data


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <training_data_json_file>")
        sys.exit(1)

    training_data_file = sys.argv[1]

    data = read_json(training_data_file)


    training_data = prepare_training_data(data)
    #Following the API, put it into a json file and use that json file instead

    with open("train_gpt_4900_two_class_4773_data.json", "w") as file:  #Change the filename here as per your need
        for entry in training_data:
            file.write(json.dumps(entry) + '\n')


    print("Fine tune started.........")


    #This is for the new upgraded openAI api
    fine_tuned_file = client.files.create(
        file = open("train_gpt_4900_two_class_4773_data.json", "rb"),  #Change the filename here as per your need
        purpose = "fine-tune"
    )

    print("Fine tune completed!")


    fine_tuned_file_id = fine_tuned_file.id

    print("This is the fine tune file id : " + fine_tuned_file_id)


    #This is how it's done in the new upgraded model
    fine_tuned_job = client.fine_tuning.jobs.create(training_file=fine_tuned_file_id, model="gpt-3.5-turbo-1106") #prev gpt-3.5-turbo
    fine_tuned_job_id = fine_tuned_job.id

    print("This is the fine tuned job-id : ", fine_tuned_job_id)
