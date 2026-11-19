from openai import AzureOpenAI
endpoint = "https://project25115-resource.services.ai.azure.com/"
api_key = "1KpC5N5678932466803Oy0qPorsV2tYmoDeSOAiopty544332qqJQQJ99CKACE1PydXJ3w3AAAAACOGsTKZ"
deployment_name = "gpt-5-mini"
#key phrase extraction from user content 

from openai import AzureOpenAI

# 1. Endpoint should be the "Endpoint" or "Target URI" found in the Azure portal
# Format is typically: https://<your-resource-name>.openai.azure.com/
# Or the new format: https://<your-resource-name>.services.ai.azure.com/
endpoint = "https://project25115-resource.services.ai.azure.com/"

# 2. API Key (please ensure it is not leaked)
api_key = "1KpC5N3S76nK55GTEJ3Oy0qPorsV2tYmoDeSOAUNDj0Hjc8C6bqqJQQJ99CKACE1PydXJ3w3AAAAACOGsTKZ"

# 3. Deployment Name: fill in the deployment name you set in Azure AI Foundry
# It may be different from the model name (gpt-5-mini), be sure to verify
deployment_name = "gpt-5-mini"  # Please confirm this is your deployment name
# 4. Use AzureOpenAI client
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=api_key,
    api_version="2024-12-01-preview"  # Use a recent stable API version
)

# 5. Call the model (model parameter uses deployment name)
response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {"role": "system", "content": "you are an AI assistent extract only key phrases from user content"},
        {"role": "user", "content": "location of MITS college"}
    ]
)

print(response.choices[0].message.content)
