from pymongo import MongoClient
import os

# Connect to MongoDB
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client['finance_bot']

# Collections
transactions = db['transactions']
budgets = db['budgets']

def store_expense(user, data):
    """Store a transaction (spent/received) in MongoDB"""
    transactions.insert_one({"user": user, **data})

def get_transactions(user):
    """Retrieve all transactions for a user"""
    return list(transactions.find({"user": user}))

def set_budget(user, amount):
    """Set a budget for a user"""
    budgets.update_one({"user": user}, {"$set": {"amount": amount}}, upsert=True)

def get_budget(user):
    """Get the budget of a user"""
    data = budgets.find_one({"user": user})
    return data["amount"] if data else "No budget set"
