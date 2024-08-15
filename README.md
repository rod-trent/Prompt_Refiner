# Prompt Refiner
A web-based tool to create better prompts.

Prompt Refiner, the ultimate app for enhancing your AI interactions. With a user-friendly form for input, Prompt Refiner invites you to submit your initial ideas or questions. Leveraging the advanced capabilities of OpenAI’s GPT-3, the app processes your input, refining it into a clear, concise, and optimized prompt. Experience the satisfaction of seeing your thoughts transformed as Prompt Refiner displays the polished prompt, ready for any AI-powered application. Elevate your AI experience with Prompt Refiner – where your input becomes inspiration.

Code here: https://github.com/rod-trent/GenAI_Prompt_Refiner/tree/main/Code

Here is a step-by-step guide:

1. Set up the Flask application.
2. Create a form for user input.
3. Process the input and refine the prompt using OpenAI's GPT-3.
4. Display the refined prompt to the user.

Required packages:

```python
pip install flask openai
```

If you've not already, set up Azure OpenAI: Ensure you have an Azure subscription and have deployed the OpenAI service in Azure. Obtain the endpoint URL and API key from the Azure portal.

Modify the BestPrompt.py script and replace the placeholders with your actual Azure OpenAI endpoint, API key, and deployment name.

**Placeholders:** 
* azure_openai_endpoint: The endpoint URL for your Azure OpenAI service.
* azure_openai_api_key: The API key for your Azure OpenAI service.
* deployment_name: The name of your deployment in Azure OpenAI.

Run the application

```python
python BestPrompt.py
```

This will start a local web server. Open your web browser and navigate to http://127.0.0.1:5000/ to access the web app. You can enter a prompt, and the app will refine it using Azure OpenAI and display the refined prompt.
