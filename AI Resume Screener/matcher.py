import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

SKILL_KEYWORDS = [
    "python", "java", "sql", "excel", "tableau", "power bi", "machine learning",
    "deep learning", "nlp", "data analysis", "statistics", "selenium", "salesforce",
    "apex", "lwc", "javascript", "html", "css", "git", "jira", "manual testing",
    "automation testing", "api testing", "rest api"
]


def extract_skills(text):
    lower_text = text.lower()
    found = []
    for skill in SKILL_KEYWORDS:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, lower_text):
            found.append(skill.title())
    return found


def get_recommendation(score):
    if score >= 80:
        return "Strong Match"
    if score >= 60:
        return "Moderate Match"
    return "Weak Match"


def rank_resumes(job_description, resume_records):
    documents = [job_description] + [record["cleaned_text"] for record in resume_records]
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(documents)
    jd_vector = vectors[0:1]
    resume_vectors = vectors[1:]
    scores = cosine_similarity(jd_vector, resume_vectors).flatten() * 100

    rows = []
    for record, score in zip(resume_records, scores):
        rows.append(
            {
                "Resume Name": record["file_name"],
                "Match Score (%)": round(float(score), 2),
                "Matched Skills": record["skills"],
            }
        )

    df = pd.DataFrame(rows).sort_values(by="Match Score (%)", ascending=False).reset_index(drop=True)
    return df