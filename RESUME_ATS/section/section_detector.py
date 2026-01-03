import re

SECTION_HEADERS = {
    "skills": ["skills", "technical skills", "core skills"],
    "experience": ["experience", "work experience", "employment", "work history"],
    "education": ["education", "academic", "qualification"],
    "projects": ["projects", "personal projects"]
}

def detect_sections(text):
    lines = text.split(" ")
    sections = {k: "" for k in SECTION_HEADERS}
    current_section = None

    for word in lines:
        for sec, keys in SECTION_HEADERS.items():
            if word in keys:
                current_section = sec

        if current_section:
            sections[current_section] += word + " "

    return sections
