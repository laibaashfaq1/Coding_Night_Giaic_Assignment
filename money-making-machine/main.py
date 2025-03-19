import streamlit as st
import random
import time
import requests

# Set the title of the web app
st.title("Money Making Machine 💰")

def generate_money():
    return random.randint(1,1000) # Generate a random amount between 1 and 1000

# Set the Subheader
st.subheader("Instant Cash Gernerator")

# Set the button to generate money
if st.button("Generate Money"):
    st.write("Generate Money")
    
    # Delay the generation of money  for 1 second
    time.sleep(1)
    amount = generate_money()
    st.success(f"You have generated ${amount}!")
    
# Fetch side hustle ideas from the FastAPI app
def fetch_side_hustle():
    try:
        response = requests.get('http://127.0.0.1:8000/side_hustle')
        if response.status_code==200:
            hustles = response.json()
            return hustles["side_hustle"]
        else:
            return ("Freelancing")

    except:
        return ("No side hustle found")
    
# Set the subheader for side hustle
st.subheader("Side Hustle Ideas")

# Set the button to show a side hustle
if st.button("Show me a side hustle"):
    idea = fetch_side_hustle()
    st.info(f"{idea}")


# Fetch money quote ideas from the FastAPI app
def fetch_money_quote():
    try:
        response = requests.get('http://127.0.0.1:8000/money_quotes')
        if response.status_code==200:
            hustles = response.json()
            return hustles["money_quote"]
        else:
            return ("Money is only a tool. It will take you wherever you wish, but it will not replace you as the driver. - Ayn Rand")

    except:
        return ("Something went wrong")
    
# Set the subheader for money quote
st.subheader("Money Quote Ideas")

# Set the button to show a money quote
if st.button("Show me a money quote"):
    quote = fetch_money_quote()
    st.info(f"{quote}")
