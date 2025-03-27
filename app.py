from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from config import TWILIO_WHATSAPP_NUMBER
import google.generativeai as genai
import os
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime

# Load API Key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# MongoDB Connection URI
uri = "mongodb+srv://hackathon:hack123@cluster0.wnxeld3.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["MoneyMitra"]  # Database name
expenses_collection = db["expenses"]

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

def parse_transaction(ai_response):
    """Extract structured data from AI response"""
    lines = ai_response.split("\n")
    data = {}
    for line in lines:
        if "Transaction Type" in line:
            data["type"] = line.split(":")[-1].strip().lower()
        elif "Amount" in line:
            data["amount"] = int(line.split(":")[-1].strip())
        elif "Category" in line:
            data["category"] = line.split(":")[-1].strip().lower()
    return data

def store_expense(user, data):
    """Store a transaction in MongoDB"""
    transaction = {
        "user": user,
        "type": data["type"],
        "amount": data["amount"],
        "category": data["category"],
        "date": datetime.utcnow()
    }
    expenses_collection.insert_one(transaction)

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def whatsapp_webhook():
    """Handles incoming WhatsApp messages"""
    
    incoming_msg = request.form.get('Body')
    sender = request.form.get('From')

    response = MessagingResponse()
    msg = response.message()

    ai_response = analyze_message(incoming_msg)

    # If AI detects a transaction, store it in MongoDB
    if "Transaction Type" in ai_response:
        data = parse_transaction(ai_response)
        store_expense(sender, data)
        transaction_message = f"✅ Transaction Recorded: {data['type']} ₹{data['amount']} on {data['category']}."
        msg.body(transaction_message)
    else:
        msg.body(ai_response)

    return str(response)

if __name__ == '__main__':
    app.run(debug=True)
