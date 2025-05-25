import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = {
    "GROQ_API_KEY"      : os.getenv("GROQ_API_KEY"),
    "TOGETHER_API_KEY"  : os.getenv("TOGETHER_API_KEY")
}