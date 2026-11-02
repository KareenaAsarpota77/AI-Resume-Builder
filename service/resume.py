import requests
import os
from openai import OpenAI

base_url = os.getenv("BASE_URL")
api_key = os.getenv("API_KEY")
model = os.getenv("MODEL")

if base_url == None or api_key== None or model==None:
    print("🚨 Base URL or API Key or Model not found!!!")

def get_answers(question:str):
    ollama = OpenAI(
        base_url=base_url,
        api_key=api_key
    )

    response = ollama.chat.completions.create(
        model=model,
        messages= [
            {
                "role" : "system",
                "content" : "You are an AI assistant that helps to improve resumes, tailor resumes for specific job descriptions, and provide ATS scores for resumes. Do not provide any other information or answer any other questions. Only respond to questions related to resume improvement, tailoring resumes for job descriptions, and providing ATS scores. Do not make up any information relating to skills, qualificaltions, etc... If the question is not related to resume improvement, tailoring resumes for job descriptions, or providing ATS scores, respond with 'I'm sorry, I can only help with resume improvement, tailoring resumes for job descriptions, and providing ATS scores"
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response.choices[0].message.content

