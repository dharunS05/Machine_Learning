import spacy

nlp = spacy.load("en_core_web_sm")

def load_skills(path="E:\Git_Programs\Resume_Analyser\skills\skill_list.txt"):
    with open(path) as f:
        return [skill.strip().lower() for skill in f.readlines()]

SKILL_DB = load_skills()

def extract_skills(text):
    text = text.lower()
    found_skills = set()

    for skill in SKILL_DB:
        if skill in text:
            found_skills.add(skill)

    return list(found_skills)
