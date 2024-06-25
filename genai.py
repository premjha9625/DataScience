from flask import Flask, jsonify, request
import google.generativeai as genai
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Configure genai with Google API Key
api_key = os.getenv("GOOGLE_API_KEY")
if api_key is None:
    raise ValueError("Google API Key not found in environment variables.")

genai.configure(api_key=api_key)

@app.route('/generate', methods=['POST'])
def generate_response():
    # Get prompt from request JSON
    prompt = request.json.get('prompt')

    # Generate content using GenAI
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)

    # Return the generated text as JSON response
    return jsonify({'generated_poem': response.text})

if __name__ == '__main__':
    app.run(debug=True)
