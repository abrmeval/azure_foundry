import os
import base64
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()   

# Required environment variables (example names)
foundry_key=os.getenv("AZURE_FOUNDRY_API_KEY")
endpoint=os.getenv("AZURE_FOUNDRY_ENDPOINT")
model_name=os.getenv("AZURE_FOUNDRY_DEDICATED_MODEL")  # e.g., "gpt-image-1"

client = OpenAI(
    api_key=foundry_key,
    base_url=endpoint,
)

prompt = "A modern flat illustration of a robot holding a potted plant, clean vector style, pastel colors."

response = client.responses.create(
    model=model_name,  # your deployment name in Foundry
    input=prompt,
    tools=[{"type": "image_generation"}],
)

image_base64 = next(
    item.result for item in response.output
    if item.type == "image_generation_call"
)

with open("foundry_generated.png", "wb") as f:
    f.write(base64.b64decode(image_base64))

print("Saved: foundry_generated.png")