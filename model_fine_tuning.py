import os
import openai
from dotenv import load_dotenv
import time

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

file_path = "file.jsonl"
print(f"Uploading file: {file_path}")
file_response = openai.files.create(file=open(file_path, "rb"), purpose="fine-tune")
file_id = file_response.id
print(f"Uploaded file ID: {file_id}")
print("Starting fine-tune...")
fine_tune_response = openai.fine_tuning.jobs.create(training_file=file_id, model="gpt-3.5-turbo")
job_id = fine_tune_response.id
print(f"Fine-tune job started with ID: {job_id}")
while True:
    job = openai.fine_tuning.jobs.retrieve(job_id)
    print(f"Status: {job.status}")
    if job.status in ["succeeded", "failed", "cancelled"]:
        print("Fine-tuning finished.")
        print(f"Model: {job.fine_tuned_model}")
        break
    time.sleep(10)
