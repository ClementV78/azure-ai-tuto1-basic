from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import ConnectionType
from azure.identity import DefaultAzureCredential
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
from azure.ai.inference.models import SystemMessage, UserMessage
import openai


try:
    # Get project client
    project_connection_string = "eastus.api.azureml.ms;602ce108-f886-44a7-bbc8-6c83e4cc2401;rg-clem0x-8057_ai;clem0x-azure-ai-foundry-sdk"

    project_client = AIProjectClient.from_connection_string(
      credential=DefaultAzureCredential(),
      conn_str=project_connection_string,
    )

    # Get the properties of the default Azure AI Services connection with credentials
    connection = project_client.connections.get_default(
      connection_type=ConnectionType.AZURE_AI_SERVICES,
      include_credentials=True, 
    )

    # Use the connection information to create a text analytics client
    ai_svc_credential = AzureKeyCredential(connection.key)
    text_analytics_client = TextAnalyticsClient(endpoint=connection.endpoint_url, credential=ai_svc_credential)

    # Menu for choosing between sentiment analysis and chat with a generative AI model
    print("Choisissez une option :")
    print("1. Analyse de sentiment")
    print("2. Discuter avec un modèle IA génératif (Azure AI Inference, ex: phi-4)")
    print("3. Discuter avec GPT-4 (Azure OpenAI, client dédié)")
    choix = input("Votre choix (1/2/3) : ")

    if choix == "1":
        # Analyse de sentiment
        text = input("Entrez le texte à analyser : ")
        sentimentAnalysis = text_analytics_client.analyze_sentiment(documents=[text])[0]
        print("Texte : {}\nSentiment : {}".format(text, sentimentAnalysis.sentiment))
    elif choix == "2":
        # Discussion avec un modèle IA génératif
        chat = project_client.inference.get_chat_completions_client()
        print("Chat client :", chat)
        print("Endpoint utilisé pour le chat :", connection.endpoint_url)
        user_prompt = input("Entrez une question : ")
        response = chat.complete(
            model="phi-4",
            messages=[
                SystemMessage("Tu parle commme le professeur tournesol dans tintin et répond de manniere amusante"),
                UserMessage(user_prompt)
            ],
        )
        print(response.choices[0].message.content)
    elif choix == "3":
        # Discussion avec GPT-4 via Azure OpenAI
        openai_client = project_client.inference.get_azure_openai_client(api_version="2024-06-01")
        user_prompt = input("Entrez une question : ")
        response = openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Tu parle commme le capitaine haddock qui aurait abusé de la bouteille dans tintin et répond de manniere amusante"},
                {"role": "user", "content": user_prompt},
            ]
        )
        print(response.choices[0].message.content)
    else:
        print("Choix invalide.")

except Exception as ex:
    print(ex)
