import sys
import openai
import csv
from openai import OpenAI

OPENAI_API_KEY = "key-here"      #Nwafor paid gpt-4.0
client = OpenAI(api_key=OPENAI_API_KEY)

########################################
#USe this code only if you're testing a single input
# only change the part below this line

# def ask_gpt_question(sample_input):
#     print("Hello one")
#     # Generate predicted output for the sample input
#     #fine_tuned_model_id = "ft:gpt-3.5-turbo-0613:personal::8E8hgIg2"   #one
#     #fine_tuned_model_id = "ftjob-Sxa9S5B9xIiRGvmUbi5d0Qg7"  #one
#     #fine_tuned_model_id = "ft:gpt-3.5-turbo-0613:personal::8GCoKdm6"  #Latest trained nwafor
#     #fine_tuned_model_id = "ft:gpt-3.5-turbo-0613:personal::8E8t47mZ"
#     fine_tuned_model_id = "ft:gpt-3.5-turbo-0613:personal::8LOCIW5L"

#     response = openai.ChatCompletion.create(
#         model=fine_tuned_model_id,
#         messages=[
#             {"role": "system", "content": "What will be the output of the user provided input; malicious or not?"},
#             {"role": "user", "content": sample_input}
#         ],
#         #max_tokens=50
#     )

#     print("Hello two")

#     # Print the predicted output
#     predicted_output = response.choices[0].message
#     print("Predicted output for the sample input:")
#     print(predicted_output)


# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print("Usage: python3 ask_gpt.py <enter your input to chat gpt>")
#         sys.exit(1)

#     user_input = sys.argv[1]

#     ask_gpt_question(user_input)
 
#sample input command in terminal   
#python3 ask_gpt.py "3 4 4 0.510989 192.168.0.1 192.168.0.13 ICMP 146 0 1 6 7"

######################################################################################
# USe the code above this line when you want to test just one input. If you're 
# testing from a whole file, use the code below


def ask_gpt_question(sample_file):
    print("Hello one")
    #If you want to test another model check the file named "all_models_ids.txt"
    fine_tuned_model_id = "ft:gpt-3.5-turbo-1106:personal::8yOe749j" #Multi class smote numeric
 

    with open(sample_file, newline='') as csvfile_input, open("answers_multiclass_smote.csv", mode='w', newline='') as csvfile_output:
        reader = csv.reader(csvfile_input)
        writer = csv.writer(csvfile_output)
        writer.writerow(["input_data", "label", "predicted_label"])
        next(reader, None)  # Skips the header row

        # Loop over each row in the input CSV
        i = 0
        for row in reader:
            test_value = row[0]
            current_label = row[1]
            response = client.chat.completions.create(
                model=fine_tuned_model_id,
                messages=[
                    {"role": "system", "content": "What will be the output of the system when processing the given input; 'DoS', 'MIRAI', 'Recon', 'Web-Based', 'Spoofing', 'BenignTraffic', 'Brute_Force'?"},
                    {"role": "user", "content": test_value}
                ],
            )
            output = response.choices[0].message.content.strip()
            print(output)
            predictedValue = output
            i += 1
            if (i % 100 == 0):
                print(predictedValue)
                print("Rows processed = ", i)

            # Write a new row to the output CSV file 
            writer.writerow([test_value, current_label, predictedValue])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 ask_gpt.py <enter your filename as an input to chat gpt>")
        sys.exit(1)

    user_input = sys.argv[1]

    ask_gpt_question(user_input)
