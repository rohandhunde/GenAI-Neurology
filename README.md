# GenAI-Numarology
A FastAPI-based Numerology API that calculates Life Path, Destiny &amp; Soul Urge numbers with Sanatan Dharma-based spiritual insights.

## 📦 Setup Instructions

### 🔹 Step 1: Create a Virtual Environment
python -m venv venv

### Step 2: Activate the Virtual Environment
.\venv\Scripts\activate

### Step 3: Install Required Packages
pip install -r requirements.txt

### Stem 4: create .env file and put your groq_api key like following
GROQ_API_KEY="your_api_key

✅ Option 1: See Output in Terminal
python Numarology.py

🌐 Option 2: Access API via Swagger UI
Run the following command:
uvicorn NumarologyAPI:app --reload
Once the server is running, press Ctrl + Click (or manually open) the following URL in your browser:
http://127.0.0.1:8000
Then, navigate to the Swagger documentation by appending /docs:

http://127.0.0.1:8000/docs
In the Swagger UI:
Click on numerology > Try it out
Enter the required information (Full Name and Date of Birth)
Click Execute to get your numerology result


