import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

endpoint = os.getenv("AZURE_FOUNDRY_ENDPOINT")
deployment_name = "DeepSeek-V4-Flash"
api_key = os.getenv("AZURE_FOUNDRY_API_KEY")

client = OpenAI(
    base_url=endpoint,
    api_key=api_key,
)

completion = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {
            "role": "system",
            "content": "You are a helpful AI assistant who supports employees with expense claims. Provide concise, accurate information only on topics related to expenses. Do not provide any information about topics that are not directly related to expenses.",
        },
        {
            "role": "user",
            "content": "What is the capital of France?",
        },
    ],
)

print(completion.choices[0].message.content)
