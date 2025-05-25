import os
from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
    
client = OpenAI(
  api_key=os.getenv("GROK_API_KEY"),
  base_url="https://api.x.ai/v1",
)

completion = client.chat.completions.create(
  model="grok-3",
  messages=[
    {"role": "user", "content": "What is the meaning of life?"}
  ]
)