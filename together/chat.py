from together import Together
from dotenv import load_dotenv
import os

load_dotenv()

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

#client = Together()

#response = client.chat.completions.create(
#    model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
#    messages=[{"role": "user", "content": "What are some fun things to do in New York?"}],
#)
#print(response.choices[0].message.content)

client = Together()

message = [{'role': 'user', 'content': 'Whats the date and time?'}]

response = client.chat.completions.create(
    model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
    messages=message,
    max_tokens=None,
    temperature=0.7,
    top_p=0.7,
    top_k=50,
    repetition_penalty=1,
    stop=["<｜end▁of▁sentence｜>"],
    stream=True
)
for token in response:
    if hasattr(token, 'choices'):
        print(token.choices[0].delta.content, end='', flush=True)