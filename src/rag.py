from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import ConnectionType
import openai


# Initialize the project client
projectClient = AIProjectClient.from_connection_string(
    conn_str="<region>.api.azureml.ms;<project_id>;<hub_name>;<project_name>",
    credential=DefaultAzureCredential()
)

# Get an Azure OpenAI chat client
chat_client = projectClient.inference.get_azure_openai_client(api_version="2024-10-21")

# Use the AI search service connection to get service details
searchConnection = projectClient.connections.get_default(
    connection_type=ConnectionType.AZURE_AI_SEARCH,
    include_credentials=True,
)
search_url = searchConnection.endpoint_url
search_key = searchConnection.key

# Initialize prompt with system message
prompt = [
    {"role": "system", "content": "You are a helpful AI assistant."}
]

# Add a user input message to the prompt
input_text = input("Enter a question: ")
prompt.append({"role": "user", "content": input_text})

# Additional parameters to apply RAG pattern using the AI Search index
rag_params = {
    "data_sources": [
        {
            "type": "azure_search",
            "parameters": {
                "endpoint": search_url,
                "index_name": "<azure_ai_search_index_name>",
                "authentication": {
                    "type": "api_key",
                    "key": search_key,
                }
            }
        }
    ],
}

# Submit the prompt with the index information
response = chat_client.chat.completions.create(
    model="<model_deployment_name>",
    messages=prompt,
    extra_body=rag_params
)

# Print the contextualized response
completion = response.choices[0].message.content
print(completion)