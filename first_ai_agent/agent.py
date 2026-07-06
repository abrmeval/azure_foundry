# Before running the sample:
#    pip install azure-ai-projects>=2.1.0

# The code to connect to your agent uses the Azure.AI.Projects library to create an AIProjectClient object connected to your Foundry project.
# Since this involves connecting to a project, which may contain privileged resources, key-based authentication is not supported, and the application must use an Entra ID identity to be authenticated.

#he code uses the project client’s get_openai_client method to retrieve an OpenAI client object; with which it can submit prompts to the agent using the same Responses API 
import os    
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

endpoint = os.getenv("AZURE_FOUNDRY_ENDPOINT")

project_client = AIProjectClient(
    endpoint=endpoint,
    credential=DefaultAzureCredential(),
)

my_agent = "expense-agent"
my_version = "1"

openai_client = project_client.get_openai_client()

# Reference the agent to get a response
response = openai_client.responses.create(
    input=[{"role": "user", "content": "Tell me what you can help with."}],
    extra_body={"agent_reference": {"name": my_agent, "version": my_version, "type": "agent_reference"}},
)

print(f"Response output: {response.output_text}")