import openai
import json
import sys

#This code is to use the json file and finetune the model using the 

# Set OpenAI API key
#api_key = "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"      #Ujjwal
#api_key = "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"     #Nwafor
api_key = "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"      #ujjwal paid
openai.api_key = api_key

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
        if i < 105:
            #This is for other legacy models like babbage
            # training_data.append({
            #     'prompt': item['input_data'],
            #     'completion': item['label']
            # })

            #This is for Chat
            training_data.append({
                "messages": [{"role": "system", "content": "This chatbot predicts whether an IOT connection is malicious or not based on the inputs given to it by the user."},
                {"role" : "user", "content": item['input_data']},
                {"role" : "assistant", "content" : item['label']}
                ]
            })
            i += 1
        if i % 1000 == 0:
            print("So far {} rows training completed! ".format(i))
        if i == 100:
            break

    return training_data

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <training_data_json_file>")
        sys.exit(1)

    training_data_file = sys.argv[1]

    data = read_json(training_data_file)


    training_data = prepare_training_data(data)
    print(training_data[:10])
    print(len(training_data))

    #Following the API, put it into a json file and use that json file instead

    with open("mydata_bert_3_5.json", "w") as file:
        for entry in training_data:
            file.write(json.dumps(entry) + '\n')


    print("Fine tune started.........")
    # Fine-tune the model
    fine_tuned_file = openai.File.create(
        file = open("mydata_bert_3_5.json", "rb"),
        purpose = "fine-tune"
    )

    print("Fine tune completed!")


    fine_tuned_file_id = fine_tuned_file.id

    print("This is the fine tune file id : " + fine_tuned_file_id)

    #Create a fine tune model
    # fine_tuned_job = openai.FineTuningJob.create(training_file=fine_tuned_file_id, model="babbage-002")
    fine_tuned_job = openai.FineTuningJob.create(training_file=fine_tuned_file_id, model="gpt-3.5-turbo")
    fine_tuned_job_id = fine_tuned_job.id

    print("This is the fine tuned job-id : ", fine_tuned_job_id)
    # Retrieve the state of a fine-tune
    # openai.FineTuningJob.retrieve(fine_tuned_job_id)


    # print("This is the fine_tuned_job id : ", fine_tuned_job_id )
