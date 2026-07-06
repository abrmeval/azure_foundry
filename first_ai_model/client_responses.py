import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


endpoint = os.getenv("AZURE_FOUNDRY_ENDPOINT")
deployment_name = "DeepSeek-V4-Flash"
api_key = os.getenv("AZURE_FOUNDRY_API_KEY")

client = OpenAI(base_url=endpoint, api_key=api_key)

response = client.responses.create(
    model=deployment_name,
    instructions="You are a helpful AI assistant who supports employees with expense claims. Provide concise, accurate information only on topics related to expenses. Do not provide any information about topics that are not directly related to expenses.",
    input="What is the capital of France?",
)

print(f"answer: {response.output[0]}")
