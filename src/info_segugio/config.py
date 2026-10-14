import os
from dotenv import load_dotenv

load_dotenv()


# class Config:
#     LLM_MODEL = "llama3.2"
#     LLM_MODEL_LOW = "llama3.2"
#     AI_API_URL = "http://localhost:11434/v1"
#     AI_API_KEY = "ollama"



class Config:
    LLM_MODEL = "gpt-4o"
    LLM_MODEL_LOW = "gpt-4o-mini"
    AI_API_URL = os.getenv("AI_API_URL", "https://api.openai.com/v1/")
    AI_API_KEY = os.getenv("AI_API_KEY")
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")