import os
import base64
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()   

endpoint = os.getenv("AZURE_FOUNDRY_ENDPOINT")
deployment_name = os.getenv("AZURE_FOUNDRY_DEPLOYMENT_NAME")
api_key = os.getenv("AZURE_FOUNDRY_API_KEY")

client = OpenAI(base_url=endpoint, api_key=api_key)

img = client.images.generate(
    model=deployment_name,
    prompt="A cute baby polar bear",
    n=1,
    size="256x256",
)

image_bytes = base64.b64decode(img.data[0].b64_json)
with open("output.png", "wb") as f:
    f.write(image_bytes)
