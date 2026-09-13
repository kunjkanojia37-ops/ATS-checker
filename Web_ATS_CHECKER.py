import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from pypdf import PdfReader  # Better for reading Streamlit memory buffers
from dotenv import load_dotenv

load_dotenv()

# 1. Page Configuration
st.set_page_config(page_title="ATS Resume Evaluator", page_icon="📄")
st.title("📄 Welcome to the Resume Evaluator!")

# Instructions Expandable block to keep UI clean
with st.expander("ℹ️ Instructions", expanded=True):
    st.write("1. Upload the candidate's resume in **PDF format**.")
    st.write("2. Paste the **Job Description** text into the input box.")
    st.write("3. Click **Evaluate Resume** to get an ATS breakdown.")

# 2. Setup LLM Chain
llm = ChatGroq(model_name="openai/gpt-oss-120b")
OUTPUT_PARSER = StrOutputParser()

prompt_template = ChatPromptTemplate.from_messages([
    ("system", ( 
        "You are an ATS (Applicant Tracking System) that helps recruiters evaluate job candidates based on their resumes and job descriptions. "
        "Show a percentage match with the job description and provide a brief summary of the candidate's strengths and weaknesses. "
        "Suggest improvements to the resume to better match the job description in bullet points."
    )),
    ("user", "Please evaluate the following resume against the job description provided.\n\nResume:\n{resume}\n\nJob Description:\n{job_description}")
])

chain_output = prompt_template | llm | OUTPUT_PARSER

# 3. Streamlit Layout / Side-by-Side Inputs
col1, col2 = st.columns(2)

with col1:
    st.subheader("Candidate Resume")
    resume_input = st.file_uploader("Upload resume PDF", type=["pdf"])

with col2:
    st.subheader("Job Requirement")
    full_job_description_text = st.text_area("Paste job description here", height=200)

# 4. Processing Action
if st.button("🚀 Evaluate Resume", type="primary"):
    if not resume_input:
        st.error("Please upload a resume PDF file first.")
    elif not full_job_description_text.strip():
        st.error("Please provide a job description.")
    else:
        with st.spinner("Analyzing profile against requirements..."):
            try:
                # Read PDF from Streamlit's file uploader memory buffer
                pdf_reader = PdfReader(resume_input)
                full_resume_text = ""
                for page in pdf_reader.pages:
                    full_resume_text += page.extract_text() + "\n"
                
                # Double check that we actually extracted text
                if not full_resume_text.strip():
                    st.error("Could not extract text from the PDF. Is it a scanned image?")
                    st.stop()
                
                # Invoke LangChain
                result = chain_output.invoke({
                    "resume": full_resume_text, 
                    "job_description": full_job_description_text
                })
                
                # Output results elegantly
                st.success("Analysis Complete!")
                st.markdown("### 📊 Evaluation Result")
                st.write(result)
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
