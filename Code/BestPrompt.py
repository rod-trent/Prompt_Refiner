# app.py
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Set your Azure OpenAI endpoint and API key here
azure_openai_endpoint = '<your_api_endpoint>'
azure_openai_api_key = '<your_key>'
deployment_name = '<your_deployment_name>'  # The name of your deployment in Azure OpenAI

def refine_prompt(prompt):
    headers = {
        'Content-Type': 'application/json',
        'api-key': azure_openai_api_key,
    }
    data = {
        "prompt": f"Refine the following prompt to make it more effective for generating a high-quality response:\n\n{prompt}",
        "max_tokens": 100,  # Increase the max_tokens to allow for a longer response
        "temperature": 0.2,
    }
    response = requests.post(f"{azure_openai_endpoint}/openai/deployments/{deployment_name}/completions?api-version=2022-12-01", headers=headers, json=data)
    
    if response.status_code != 200:
        return f"Error: {response.status_code} - {response.text}"
    
    response_json = response.json()
    
    if 'choices' not in response_json:
        return f"Error: Unexpected response format - {response_json}"
    
    refined_prompt = response_json['choices'][0]['text'].strip()
    return refined_prompt

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_prompt = request.form['prompt']
        refined_prompt = refine_prompt(user_prompt)
        return render_template('index.html', original_prompt=user_prompt, refined_prompt=refined_prompt)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
