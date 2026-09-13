# 📄 ATS Resume Evaluator

An AI-powered Applicant Tracking System (ATS) resume evaluator built with **Streamlit**, **LangChain**, and **Mistral AI**. This application allows recruiters and job seekers to upload a candidate's resume in PDF format and evaluate it against a target job description to get a percentage match, candidate strengths/weaknesses, and actionable feedback.

---

## ✨ Features

* **PDF Resume Parsing**: Extracts raw text seamlessly from uploaded PDF files using `pypdf`.
* **AI Evaluation Engine**: Powered by LangChain and `mistral-small-2506` via standard prompt chains.
* **Match Score & Feedback**: Provides a estimated match percentage, candidate strengths/weaknesses, and tailored suggestions for resume optimization.
* **Clean UI**: Built with Streamlit for a fast, side-by-side user experience.

---

## 🛠️ Tech Stack

* **Framework**: Streamlit
* **LLM Orchestration**: LangChain Core / LangChain Mistral AI
* **Model**: Mistral AI (`mistral-small-2506`)
* **PDF Parser**: `pypdf`
* **Environment management**: `python-dotenv`

---

## 🚀 Getting Started

### Prerequisites

* **Python**: Python 3.9 or higher
* **Mistral AI API Key**: Get your free or paid API key from [Mistral AI Console](https://console.mistral.ai/).

---

### Installation

1. **Clone the repository**
   ```bash
   git clone [https://github.com/kunjkanojia37-ops/ATS-checker.git](https://github.com/kunjkanojia37-ops/ATS-checker.git)
   cd ATS-checker

1. Create and activate a virtual environment

   macOS/Linux:

       python3 -m venv venv
       source venv/bin/activate
    
    Windows:
       python -m venv venv
       venv\Scripts\activate

2. Install dependencies
      
      pip install streamlit langchain-core langchain-mistralai pypdf python-dotenv

3. Set up Environment Variables
   Create a .env file in the root directory of your project:
       
       GROQ_API_KEY=your_groq_api_key_her
         

🏃 Running the Application
Launch the Streamlit dashboard using:

        streamlit run app.py


Open http://localhost:8501 in your browser to start using the evaluator!

📖 How It Works
    Upload Resume: Upload candidate's resume (.pdf).

    Input Job Description: Paste the target job posting requirement text.

    Evaluate: Click 🚀 Evaluate Resume to start the LangChain execution sequence.

    Review Output: Receive a detailed evaluation report showing:

    Match percentage

    Key strengths & weaknesses

    Bulleted suggestions for alignment with ATS requirements

🛡️ License
Distributed under the MIT License. See LICENSE for more details.
