import google.generativeai as genai
import os

# Load API Key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_message(message):
    """Use Gemini AI to process messages and detect financial transactions or questions."""
    
    prompt = f"""
    You are a financial assistant. 
    - If the user logs a financial transaction like "received 100 for stipend" or "spent 100 for snacks", extract:
      - Transaction Type (Received/Spent)
      - Amount (Numeric)
      - Category (Text)
    - If the user asks a general finance question (e.g., "What is crypto?"), provide an informative answer.
    
    Message: "{message}"
    """

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    
    return response.text.strip()
