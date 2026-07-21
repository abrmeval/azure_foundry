import os
from azure.ai.contentunderstanding import ContentUnderstandingClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

load_dotenv()

endpoint = os.getenv("AZURE_FOUNDRY_ENDPOINT")
key = os.getenv("AZURE_FOUNDRY_API_KEY")

client = ContentUnderstandingClient(
    endpoint=endpoint, credential=AzureKeyCredential(key)
)

# 1) start analysis with analyzer id + inputs
analyzer_id = "prebuilt-read"
inputs = [
    {
        "url": "https://github.com/Azure-Samples/azure-ai-content-understanding-python/raw/refs/heads/main/data/invoice.pdf"
    }
]

# 2) wait for the Long Running Operation (LRO) to complete
poller = client.begin_analyze(analyzer_id=analyzer_id, inputs=inputs)  # starts LRO
result = poller.result()  # waits for completion (polling handled by SDK)

# 3) read structured fields + markdown
# The result typically includes extracted "fields" and "markdown" per input content item.
for content in result.contents:
    print(content.markdown)
    print(content.fields)
