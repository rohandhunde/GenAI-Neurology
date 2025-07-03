from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = FastAPI(title="Sanatan Dharma Numerology API")

# Pydantic model for request validation
class NumerologyInput(BaseModel):
    full_name: str
    date_of_birth: str  # Expected format: YYYY-MM-DD

# Initialize the prompt template
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

# Initialize the Grok model
model = ChatGroq(
    model="meta-llama/llama-4-maverick-17b-128e-instruct",
    temperature=0.0,
    api_key=os.getenv("GROQ_API_KEY")
)

@app.post("/numerology/")
async def get_numerology(input_data: NumerologyInput):
    try:
        # Format the prompt with user inputs
        formatted_prompt = template.format(
            full_name=input_data.full_name,
            date_of_birth=input_data.date_of_birth
        )
        
        # Invoke the model
        result = model.invoke(formatted_prompt)
        
        # Return the response
        return {"numerology_result": result.content}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

@app.get("/")
async def root():
    return {"message": "Welcome to the Sanatan Dharma Numerology API. Use POST /numerology/ with full_name and date_of_birth."}