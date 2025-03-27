from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from config import TWILIO_WHATSAPP_NUMBER
import google.generativeai as genai
import os

# Load API Key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_message(message):
    """Use Gemini AI to process messages and detect financial transactions or questions."""
    
    prompt = f"""
    You are a financial assistant. 
    If the user logs a financial transaction, extract:
      - Transaction Type (Received/Spent)
      - Amount (Numeric)
      - Category (Text)
    If the user asks a general finance question, provide an informative answer.

    Message: "{message}"
    """

    # Use the correct model name
    model = genai.GenerativeModel("gemini-1.5-flash-latest")
    response = model.generate_content(prompt)

    return response.text.strip()

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def whatsapp_webhook():
    """Handles incoming WhatsApp messages"""
    
    incoming_msg = request.form.get('Body')
    sender = request.form.get('From')

    response = MessagingResponse()
    msg = response.message()

    ai_response = analyze_message(incoming_msg)
    msg.body(ai_response)

    return str(response)

if __name__ == '__main__':
    app.run(debug=True)
