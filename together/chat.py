from together import Together
from dotenv import load_dotenv
import os

load_dotenv()

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

client = Together()

response = client.chat.completions.create(
    model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
    messages=[{"role": "user", "content": "What are some fun things to do in New York?"}],
)
print(response.choices[0].message.content)