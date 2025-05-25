import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = {
    "OPENAI_API_KEY"    : os.getenv("OPENAI_API_KEY"),
    "GROQ_API_KEY"      : os.getenv("GROQ_API_KEY"),
    "GROK_API_KEY"      : os.getenv("GROK_API_KEY"),
    "DEEPSEEK_API_KEY"  : os.getenv("DEEPSEEK_API_KEY"),
    "GOOGLE_API_KEY"    : os.getenv("GOOGLE_API_KEY"),
    "REPLICATE_API_KEY" : os.getenv("REPLICATE_API_KEY"),
    "TOGETHER_API_KEY"  : os.getenv("TOGETHER_API_KEY")
}