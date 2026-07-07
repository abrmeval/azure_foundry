import os
import base64
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

endpoint = os.getenv("AZURE_FOUNDRY_ENDPOINT")
deployment_name = os.getenv("AZURE_FOUNDRY_DEPLOYMENT_NAME")
api_key = os.getenv("AZURE_FOUNDRY_API_KEY")

client = OpenAI(base_url=endpoint, api_key=api_key)

image_path = os.path.join(os.path.dirname(__file__), "image.jpg")
with open(image_path, "rb") as f:
    image_b64 = base64.b64encode(f.read()).decode("utf-8")

response = client.responses.create(
    model=deployment_name,
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "what's in this image?"},
                {
                    "type": "input_image",
                    "image_url": f"data:image/jpeg;base64,{image_b64}",
                },
            ],
        }
    ],
)

print(f"answer: {response.output_text}")

# Previously tried to use a DeepSeek model but it returned an error:
# {'error': {'message': "Model 'DeepSeek-V4-Flash' does not support image inputs. Try again with a vision model. To find out which models are vision-enabled, visit our our models documentation: https://platform.openai.com/docs/models", 'type': 'invalid_request_error', 'param': 'input', 'code': None}}

# It prints with gpt-5-mini model:
# answer: A bowl of fruit. I can see several bananas, a couple of oranges, a lemon, an apple, and a kiwi (plus other citrus/fruit partially visible in the background). The fruits are lit with sunlight, creating strong highlights and shadows.