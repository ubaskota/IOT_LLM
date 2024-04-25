# IOT_LLM
IOT with LLM


##Use these scripts to finetune a GPT model using custom data. 

Steps involved in finetuning: 

step1: convert the csv file to a json file using the script named "csv_json.py"

step2: Next step is adding the prompt to the json file to make it suitable for finetuning. Edit the prompt in the file 
"OpenAI_finetune.py". You can also change the filenames in this script to make it different than the file obtained from step1. Otherwise the name of the training json files in this code can be same as the names of the json file obtained from step1.

step3: After you run the finetuning script from your terminal, you'll receive fine_tuned_file_id and fine_tuned_job_id. Save this for later.

step4: After the training is completed, you'll receive an email. 

step5: Use the fine_tuned_job_id you received from step3 to check how well your model performs. USe the file "ask_gpt.py" to ask questions using the model id and check the performance of your code. 



##Some sample files are as follows: 
- sample_training.csv => This is what the sample csv file used for training should look like 
- sample_training_json.json => This is what the json file should look after running the csv file through step1
- sample_training_json_openAI.json => This is what the json file should look like after you assign prompts to it and use it to finetune. This is the file that is used to finetune the gpt model. 
- sample_testing.csv => A testing file is also a csv file and it should look similar to "sample_training.csv". 
- sample_testing_converted.csv => This is what the testing file looks like after running through "ask_gpt.py"


###The file "nlp_finetune_processing_main.ipynb" is used ffor all processings including feature engineering and such. It has proper comments for you to follow.