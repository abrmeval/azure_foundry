from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("TEXT_ANALYTICS_KEY")
endpoint = os.getenv("TEXT_ANALYTICS_ENDPOINT")

# Authenticate the client using your key and endpoint 
def authenticate_client():
     ta_credential = AzureKeyCredential(key)
     text_analytics_client = TextAnalyticsClient(
             endpoint=endpoint, 
             credential=ta_credential)
     return text_analytics_client
    
client = authenticate_client()
    
# Example method for detecting sensitive information (PII) from text 
def pii_recognition_example(client):
     documents = [
         " Maria Garcia called from 020 7946 0958 and asked to send documents to 42 Market Road, London, UK, SW1A 1AA."
     ]
     response = client.recognize_pii_entities(documents, language="en")
     result = [doc for doc in response if not doc.is_error]
     for doc in result:
         print("Redacted Text: {}".format(doc.redacted_text))
         for entity in doc.entities:
             print("Entity: {}".format(entity.text))
             print(" Category: {}".format(entity.category))
             print(" Confidence Score: {}".format(entity.confidence_score))
             print(" Offset: {}".format(entity.offset))
             print(" Length: {}".format(entity.length))
pii_recognition_example(client)

## Prints:
## --------------------------------------------------
# Redacted Text:  ************ called from ************* and asked to send documents to ************************************.
#  Entity: Maria Garcia
#  Category: Person
#  Confidence Score: 1.0
#  Offset: 1
#  Length: 12
# Entity: 020 7946 0958
#  Category: PhoneNumber
#  Confidence Score: 1.0
#  Offset: 26
#  Length: 13
# Entity: 42 Market Road, London, UK, SW1A 1AA
#  Category: Address
#  Confidence Score: 1.0
#  Offset: 71
#  Length: 36
##