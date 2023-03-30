import json
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint for receiving text input from the iOS app
@app.route('/chat', methods=['POST'])
def chat():
    input_text = request.json['input_text']

    # Send a request to the ChatGPT API
    api_url = 'https://api.openai.com/v1/engines/davinci-codex/completions'
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer YOUR_API_KEY_HERE'}
    data = {
        'prompt': input_text,
        'max_tokens': 50,
        'temperature': 0.7
    }
    response = requests.post(api_url, headers=headers, data=json.dumps(data))
    generated_text = response.json()['choices'][0]['text']

    # Return the generated text to the iOS app
    return jsonify({'generated_text': generated_text})

if __name__ == '__main__':
    app.run(debug=True)
