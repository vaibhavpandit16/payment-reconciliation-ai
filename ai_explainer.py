import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# Load env variables
load_dotenv()

# Initialize client
client = OpenAI(api_key = st.secrets["OPENAI_API_KEY"])

def generate_explanation(summary):
    prompt = f"""
    You are a fintech reconciliation expert.

    Analyze the following discrepancies:
    {summary}

    Explain:
    1. Possible causes
    2. Business impact
    3. Suggested fixes
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",   # fast & cheap
        messages=[
            {"role": "system", "content": "You are a financial data analyst."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content
