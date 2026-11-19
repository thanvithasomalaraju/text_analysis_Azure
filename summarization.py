from openai import AzureOpenAI
endpoint = "https://project25115-resource.services.ai.azure.com/"
api_key = "1KpC5N3S76nK55GTEJ3Oy0qPorsyyV2tYmoDeSOAUNDj0Hjc8C6bqqJQQJ99CKACE1PydXJ3w3AAAAACOGsTKZ"
deployment_name = "gpt-5-mini"
long_text ="""Here is a long paragraph you can use for testing:

Education is one of the most powerful tools for personal and professional development. It helps individuals develop knowledge, improve communication skills, build confidence, and understand the world around them. In today's rapidly changing technological environment, learning new skills and adapting to modern technologies have become essential for success. Students should focus not only on academic performance but also on practical knowledge, creativity, critical thinking, teamwork, and problem-solving abilities. Technology has transformed almost every industry, including healthcare, agriculture, education, business, transportation, and communication. Artificial intelligence, machine learning, data science, cloud computing, and automation are creating new opportunities while also introducing challenges that require innovative solutions. Continuous learning helps individuals remain competitive and prepared for future opportunities. Educational institutions play an important role in shaping responsible citizens by providing quality education, encouraging research, promoting innovation, and creating an environment where students can explore their interests and develop their talents. Success is not achieved overnight; it requires patience, discipline, dedication, consistency, and the willingness to learn from mistakes. Every challenge provides an opportunity to gain experience, improve our abilities, and move closer to our goals. Therefore, individuals should maintain a positive attitude, set clear objectives, manage their time effectively, and work consistently toward achieving their dreams."""
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
        {"role": "system", "content": "you are a summarization assistant.summarise the content "},
        {"role": "user", "content": long_text}
    ]
)

print(response.choices[0].message.content)
