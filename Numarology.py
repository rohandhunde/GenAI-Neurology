from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
import os

from langchain.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=["full_name", "date_of_birth"],
    template="""
You are a Sanatan Dharma-based numerology expert. Given the user's full name and date of birth, perform the following:

1. Calculate and display:
   - Life Path Number
   - Destiny/Expression Number
   - Soul Urge Number

2. Recognize and highlight Master Numbers (11, 22, 33) if present.

3. Provide natural language interpretations for each number, rooted in Sanatan Dharma themes such as karma, dharma, bhakti, or gunas.

4. Suggest spiritual alignment for the user, including ruling deity, relevant mantra, or shloka references.

Respond in a warm, insightful, and spiritually uplifting tone.

User's Details:
Full Name: {full_name}
Date of Birth: {date_of_birth}
"""
)

model = ChatGroq(
    model="meta-llama/llama-4-maverick-17b-128e-instruct",
    temperature=0.0,
    api_key=os.getenv("GROQ_API_KEY")
)

# Example usage:
inputs = {
    "full_name": input("Enter your full name: "),
    "date_of_birth": input("Enter Your DOB: (YYYY-MM-DD): ")
}
result = model.invoke(template.format(**inputs))
print(result.content)