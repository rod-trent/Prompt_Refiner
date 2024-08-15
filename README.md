# Prompt Refiner (and Idea Creator)
A web-based tool to create better prompts and supply ideas for additional prompts.

Prompt Refiner - the ultimate app for enhancing your AI interactions. With a user-friendly form for input, Prompt Refiner invites you to submit your initial ideas or questions. Leveraging the advanced capabilities of Azure OpenAI’s GPT-3, the app processes your input, refining it into clear, concise, and optimized sample prompts. Experience the satisfaction of seeing your thoughts transformed as Prompt Refiner displays the polished prompts, ready for any AI-powered application. Elevate your AI experience with Prompt Refiner – where your input becomes inspiration.

## Code

Code here: https://github.com/rod-trent/GenAI_Prompt_Refiner/tree/main/Code

* Main app: https://github.com/rod-trent/GenAI_Prompt_Refiner/blob/main/Code/BestPrompt.py
* HTML template: https://github.com/rod-trent/GenAI_Prompt_Refiner/tree/main/Code/Templates

Place the main app in the main directory, the HTMl template into a \templates subdirectory.

![Directory Structure](https://github.com/rod-trent/GenAI_Prompt_Refiner/blob/main/Images/filestructure.jpg)

To increase or decrease the number of prompts in the response adjust the _max_tokens_ in the main app.  To keep the response focused on just suggested prompts instead of a lot of additional, extraneous information, the 0.1 _temperature_ tends to work well.

```python
"max_tokens": 200,
"temperature": 0.1,
```

## Requirements
Required packages:

```python
pip install flask openai
```

This solution is based on Azure OpenAI services. If you've not already, set up Azure OpenAI: Ensure you have an Azure subscription and have deployed the OpenAI service in Azure. Obtain the endpoint URL and API key from the Azure portal.

Modify the BestPrompt.py script and replace the placeholders with your actual Azure OpenAI endpoint, API key, and deployment name.

**Placeholders:** 
* azure_openai_endpoint: The endpoint URL for your Azure OpenAI service.
* azure_openai_api_key: The API key for your Azure OpenAI service.
* deployment_name: The name of your deployment in Azure OpenAI.

## Application

Run the application

```python
python BestPrompt.py
```

This will start a local web server. Open your web browser and navigate to http://127.0.0.1:5000/ to access the web app. You can enter a prompt, and the app will refine it using Azure OpenAI and display the refined prompt along with information on why the prompt is better.

![Prompt Refiner](https://github.com/rod-trent/GenAI_Prompt_Refiner/blob/main/Images/PromptRefiner.jpg)


