from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()

from router.resume import chat_router
from openai import OpenAI


app = FastAPI()

app.include_router(chat_router)

