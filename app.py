from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from config import TWILIO_WHATSAPP_NUMBER

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def whatsapp_webhook():
    """Handles incoming WhatsApp messages"""
    
    incoming_msg = request.form.get('Body')
    sender = request.form.get('From')

    response = MessagingResponse()
    msg = response.message()

    # Simple Bot Logic
    if "hello" in incoming_msg.lower():
        msg.body("Hello! 👋 I'm your personal finance assistant. How can I help you today? 😊")
    elif "bye" in incoming_msg.lower():
        msg.body("Goodbye! 👋 Stay financially smart and see you next time! 💰")
    else:
        msg.body("I'm here to help with your finances! Try saying 'log an expense', 'set a budget', or 'show my report'. 😊")

    return str(response)

if __name__ == '__main__':
    app.run(debug=True)
