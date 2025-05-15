# WhatsApp Finance Assistant

## Project Overview
WhatsApp Finance Assistant is an intelligent WhatsApp-based financial assistant that helps users track expenses, log transactions, and get financial advice using AI technology.

## Key Features
- WhatsApp messaging integration
- AI-powered transaction detection
- Expense tracking and storage
- Real-time financial insights

## Technology Stack
- **Backend**: Python, Flask
- **AI**: Google Gemini AI
- **Messaging**: Twilio WhatsApp API
- **Database**: MongoDB
- **Webhook**: ngrok (for local development)

## Prerequisites
- Python 3.8+
- Twilio Account
- Google Cloud Account
- MongoDB Atlas Account

## Setup and Installation

### 1. Clone the Repository
```bash
git clone https://github.com/prasanth-42/whatsapp-finance-assistant.git
cd whatsapp-finance-assistant
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file with the following:
```
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_WHATSAPP_NUMBER=your_twilio_whatsapp_number
GEMINI_API_KEY=your_google_gemini_api_key
MONGODB_URI=your_mongodb_connection_string
```

### 5. Ngrok Setup for Webhook
1. Download ngrok from [ngrok.com](https://ngrok.com/download)
2. Expose your local Flask server:
```bash
ngrok http 5000
```
3. Copy the generated HTTPS URL
4. Configure Twilio Webhook URL with the ngrok-generated URL + `/webhook`

### 6. Run the Application
```bash
python app.py
```

## How It Works
1. Send a message to the WhatsApp number configured in Twilio
2. The AI analyzes the message
3. For transactions, it extracts:
   - Transaction Type (Received/Spent)
   - Amount
   - Category
4. Transactions are stored in MongoDB
5. Receive instant feedback and financial insights

## Example Interactions
- "Spent 500 on groceries"
- "How much did I spend this month?"
- "Received 2000 from salary"


## Future Improvements Planned
- Add user authentication
- Implement more detailed financial analytics
- Support multiple languages
- Create a dashboard for expense tracking

## Contributing
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request
