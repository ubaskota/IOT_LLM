import sys
import openai
import csv

#api_key = "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"     #Nwafor
api_key = "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"      #ujjwal paid
openai.api_key = api_key

########################################
# only change the part below this line

# def ask_gpt_question(sample_input):
#     print("Hello one")
#     # Generate predicted output for the sample input
#     #fine_tuned_model_id = "ftjob-HsTm9Xl76LTIN2GanavVFpa3"
#     fine_tuned_model_id = "ft:gpt-3.5-turbo-0613:personal::8E8hgIg2"   #one
#     #fine_tuned_model_id = "ft:gpt-3.5-turbo-0613:personal::8E8t47mZ"

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
    # Generate predicted output for the sample input
    #fine_tuned_model_id = "ftjob-HsTm9Xl76LTIN2GanavVFpa3"
    fine_tuned_model_id = "ft:gpt-3.5-turbo-0613:personal::8E8hgIg2"   #one
    #fine_tuned_model_id = "ft:gpt-3.5-turbo-0613:personal::8E8t47mZ"


    with open(sample_file, newline='') as csvfile_input, open("gpt_returned_results.csv", mode='w', newline='') as csvfile_output:
        reader = csv.reader(csvfile_input)
        writer = csv.writer(csvfile_output)

        # Loop over each row in the input CSV
        for row in reader:
            test_value = row[0]
            response = openai.ChatCompletion.create(
                model=fine_tuned_model_id,
                messages=[
                    {"role": "system", "content": "What will be the output of the user provided input; malicious or not?"},
                    {"role": "user", "content": test_value}
                ],
            )
            output = response.choices[0].message
            print(output['content'])
            predictedValue = output['content']

            # Write a new row to the output CSV file 
            writer.writerow([test_value, predictedValue])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 ask_gpt.py <enter your filename as an input to chat gpt>")
        sys.exit(1)

    user_input = sys.argv[1]

    ask_gpt_question(user_input)
