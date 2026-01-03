import streamlit as st
import joblib

from extraction.text_extractor import extract_text
from text_cleaner.text_cleaner import clean_text
from section.section_detector import detect_sections
from skills.skill_extractor import extract_skills
from similarity.similarity_engine import semantic_similarity
from features.feature_builder import build_features

# Load trained model
model_path = r"E:\Git_Programs\Resume_Analyser\Trained_model\ats_model.pkl"
model = joblib.load(model_path)

st.title("Smart Resume ATS Predictor")

resume_file = st.file_uploader("Upload Resume (PDF/DOCX)", type=["pdf","docx"])
jd_text = st.text_area("Enter Job Description")

if st.button("Predict ATS Result"):

    if resume_file is None or jd_text.strip() == "":
        st.warning("Please upload a resume and enter a job description")
    else:
        # Save uploaded file temporarily
        with open("uploaded_resume.pdf","wb") as f:
            f.write(resume_file.getbuffer())

        raw = extract_text("uploaded_resume.pdf")
        cleaned = clean_text(raw)
        sections = detect_sections(cleaned)

        resume_skills = extract_skills(sections["skills"] + sections["experience"])
        jd_skills = extract_skills(jd_text)

        similarity = semantic_similarity(cleaned, jd_text)
        features, missing = build_features(resume_skills, jd_skills, similarity)

        data = [[
            features["skill_match_ratio"],
            features["similarity_score"],
            features["resume_skill_count"],
            features["missing_skill_count"]
        ]]

        prob = model.predict_proba(data)[0][1]  # Probability of class 1 (SHORTLIST)
        ats_score = round(prob * 100, 2)       # Convert to 0-100 scale

        status = "SHORTLIST" if ats_score >= 50 else "REJECT"  # threshold 50%

        st.subheader(f"ATS Result: {status}")
        st.write(f"ATS Score: {ats_score} / 100")
        st.write("Features:", features)
        st.write("Missing Skills:", missing)
