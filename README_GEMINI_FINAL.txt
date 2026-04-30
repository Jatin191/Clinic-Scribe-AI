CLINICAL SCRIBE AI (GEMINI VERSION) — README

OVERVIEW This project converts a doctor-patient consultation transcript
into a structured SOAP note with ICD-10 code using Gemini (free model).

FILES - app_gemini.py → Streamlit web app - clinical_scribe_gemini.py →
CLI script - requirements_gemini.txt → Dependencies - README_GEMINI.txt
→ This file

STEP 1: Install Python Install Python 3.9 or higher.

STEP 2: Install Dependencies Run in terminal: 

python -m pip install -r requirements_gemini.txt

STEP 3: Get Gemini API Key 
    1. Go to Google AI Studio 
    2. Create API key
    3. Copy the key

STEP 4: Set API Key(Optional if you want to run in virtual than do this)

 1. Windows PowerShell: $env:GEMINI_API_KEY=“your_api_key_here”
 2. Windows CMD: set GEMINI_API_KEY=your_api_key_here
 3. Mac/Linux: export GEMINI_API_KEY=“your_api_key_here”

STEP 5: Run Streamlit App 

python -m pip install -r requirements_gemini.txt
python -m streamlit run app_gemini.py

Open in browser: http://localhost:8501

STEP 6: Use Application - Choose sample consultation OR paste your own -
Click “Generate SOAP Note” - View output - Download JSON


COMMON ERRORS

1.  No module found → Run install again: python -m pip install -r
    requirements_gemini.txt

2.  GEMINI_API_KEY not set → Set environment variable again

3.  Streamlit not found → Use: python -m streamlit run app_gemini.py

NOTES - This is a demo project - Not for real clinical use - Always
verify ICD-10 codes manually

DONE — Your Gemini Clinical Scribe is ready 🚀
