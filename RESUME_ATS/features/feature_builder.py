def build_features(resume_skills, jd_skills, similarity):

    resume_skills = set(resume_skills)
    jd_skills = set(jd_skills)

    matched = resume_skills.intersection(jd_skills)
    missing = jd_skills - resume_skills

    skill_match_ratio = len(matched) / len(jd_skills) if len(jd_skills) > 0 else 0

    features = {
        "skill_match_ratio": round(skill_match_ratio,2),
        "similarity_score": round(similarity,2),
        "resume_skill_count": len(resume_skills),
        "missing_skill_count": len(missing)
    }

    return features, list(missing)
