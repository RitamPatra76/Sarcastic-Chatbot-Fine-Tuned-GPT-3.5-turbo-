# Sarcastic-Chatbot-Fine-Tuned-GPT-3.5-turbo

This project fine-tunes OpenAI’s `gpt-3.5-turbo` to create a chatbot with a sarcastic tone.  
It includes training scripts, a sample dataset, and an interface to interact with the model.
Please change the openai api key from the `.env` file with your own api key.
`app.py` is the main script to interact with the fine-tuned sarcastic chatbot.  
`file.jsonl` contains the training data used for fine-tuning in JSONL format.  
`model_fine_tuning.py` handles the file upload and fine-tuning job via OpenAI's API.  
`requirements.txt` lists the Python dependencies required to run the project.  
