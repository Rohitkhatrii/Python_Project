import io
import pandas as pd
import streamlit as st

from resume_parser import extract_text
from preprocess import clean_text
from matcher import rank_resumes, extract_skills, get_recommendation

st.set_page_config(page_title="AI-Powered Resume Screener", page_icon="📄", layout="wide")

st.title("AI-Powered Resume Screener")
st.caption("Upload resumes, paste a job description, and rank candidates using NLP, TF-IDF, and cosine similarity.")

with st.sidebar:
    st.header("Job Description")
    job_description = st.text_area(
        "Paste the job description",
        height=300,
        placeholder="Enter job title, skills, responsibilities, and qualifications...",
    )
    st.markdown("### Skill Dictionary")
    st.caption("The app highlights matched skills from a predefined list.")

uploaded_files = st.file_uploader(
    "Upload resumes (PDF or DOCX)",
    type=["pdf", "docx"],
    accept_multiple_files=True,
)

run = st.button("Screen Resumes", type="primary")

if run:
    if not job_description.strip():
        st.error("Please paste a job description.")
    elif not uploaded_files:
        st.error("Please upload at least one resume.")
    else:
        with st.spinner("Analyzing resumes..."):
            cleaned_jd = clean_text(job_description)
            resume_records = []

            for file in uploaded_files:
                raw_bytes = io.BytesIO(file.read())
                text = extract_text(file.name, raw_bytes)
                cleaned_resume = clean_text(text)
                matched_skills = extract_skills(text)
                resume_records.append(
                    {
                        "file_name": file.name,
                        "raw_text": text,
                        "cleaned_text": cleaned_resume,
                        "skills": ", ".join(matched_skills) if matched_skills else "No common skills found",
                    }
                )

            results = rank_resumes(cleaned_jd, resume_records)
            results["Recommendation"] = results["Match Score (%)"].apply(get_recommendation)
            results.index = results.index + 1
            results.index.name = "Rank"

        st.subheader("Ranked Candidates")
        st.dataframe(results, use_container_width=True)

        csv = results.to_csv(index=True).encode("utf-8")
        st.download_button(
            "Download Results as CSV",
            data=csv,
            file_name="resume_screening_results.csv",
            mime="text/csv",
        )

        top_candidate = results.iloc[0]
        st.subheader("Top Candidate")
        col1, col2, col3 = st.columns(3)
        col1.metric("Candidate", top_candidate["Resume Name"])
        col2.metric("Match Score", f"{top_candidate['Match Score (%)']}%")
        col3.metric("Recommendation", top_candidate["Recommendation"])

        with st.expander("View extracted skills"):
            for idx, row in results.iterrows():
                st.markdown(f"**{row['Resume Name']}** — {row['Matched Skills']}")
else:
    st.info("Add a job description and upload resumes, then click **Screen Resumes**.")