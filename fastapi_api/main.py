from fastapi import FastAPI
import random

# Create a FastAPI instance
app = FastAPI()

# we will build two simple get endpoints
# side_hustle
# money_quotes
side_hustles = [
    ("Freelancing", "Earn money by doing freelance work"),
    ("Dropshipping", "Sell products without holding inventory"),
    ("Affiliate Marketing", "Promote products and earn commissions"),
    ("Crypto Trading", "Buy and sell cryptocurrencies"),
    ("Online Courses", "Create and sell online courses"),
    ("YouTube", "Create a YouTube channel and earn money from ads"),
    ("Graphic Design", "Create custom-designed graphics for businesses"),
    ("App Development", "Create mobile or web apps for businesses")
]

# List of money quotes
money_quotes = [
    "The more you learn, the more you earn. - Warren Buffett",
    "Money is only a tool. It will take you wherever you wish, but it will not replace you as the driver. - Ayn Rand",
    "Don't work for money; make money work for you. - Robert Kiyosaki",
    "The best investment you can make is in yourself. - Warren Buffett",
    "Money is a terrible master but an excellent servant. - P.T. Barnum",
    "Never spend your money before you have earned it. - Thomas Jefferson",
    "It's not how much money you make, but how much money you keep. - Robert Kiyosaki",
    "An investment in knowledge pays the best interest. - Benjamin Franklin",
    "The goal isn't more money. The goal is living life on your terms. - Chris Brogan",
    "Time is more valuable than money. You can get more money, but you cannot get more time. - Jim Rohn"
]

@app.get("/side_hustle")
def get_side_hustle(apiKey: str):
    """Get a random side hustle idea"""
    # This key is requird for accessing the API
    if apiKey != "12345678":
        return {"error": "Invalid API key"}
    return {"side_hustle": random.choice(side_hustles)}

@app.get("/money_quotes")
def get_money_quotes(apiKey: str):
    """Returns a random money quote"""
    # This key is requird for accessing
    if apiKey!= "12345678":
        return {"error": "Invalid API key"}
    return {"money_quote": random.choice(money_quotes)}
