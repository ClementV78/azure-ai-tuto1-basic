# Azure AI Project Demo

Ce projet Python propose une démonstration de l'utilisation des services Azure AI pour :

- L'analyse de sentiment de texte (Azure AI Text Analytics)
- La discussion avec un modèle génératif déployé via Azure AI Inference (ex : phi-4)
- La discussion avec GPT-4 via Azure OpenAI (client dédié)

## Prérequis

- Python 3.8+
- Un environnement virtuel Python (`.venv` recommandé)
- Un projet Azure Machine Learning avec les connexions nécessaires (Azure AI Services, Azure AI Inference, Azure OpenAI)
- Les clés et chaînes de connexion Azure correspondantes

## Installation

1. Clonez ce dépôt :
   ```sh
   git clone <url-du-repo>
   cd azure-ai-1
   ```
2. Créez et activez un environnement virtuel :
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Installez les dépendances :
   ```sh
   pip install azure-ai-projects azure-ai-inference azure-ai-textanalytics azure-identity
   ```

## Utilisation

Lancez le script principal :
```sh
python src/main.py
```

Vous pourrez alors choisir :
1. Analyse de sentiment
2. Discuter avec un modèle IA génératif (Azure AI Inference, ex: phi-4)
3. Discuter avec GPT-4 (Azure OpenAI, client dédié)

## Configuration

- Modifiez la variable `project_connection_string` dans `src/main.py` avec la chaîne de connexion de votre projet Azure.
- Assurez-vous d'être authentifié auprès d'Azure (via `az login` ou variables d'environnement pour un Service Principal).

## Exemple de structure du projet

```
azure-ai-1/
├── src/
│   ├── main.py
│   └── rag.py
├── .venv/
└── azure-ai-1.code-workspace
```

## Ressources utiles
- [Documentation Azure AI Projects](https://learn.microsoft.com/azure/machine-learning/)
- [SDK Azure pour Python](https://learn.microsoft.com/python/api/overview/azure/)

---

© 2025 - Projet démo Azure AI
