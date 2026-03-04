from app.agents.resume_analyzer import analyze_resume

if __name__ == "__main__":
    sample_resume_text = """
    - Software engineer with 4 years of experience.
    - Skilled in C++ and Java.
    - Worked at ABC Corp as a software Developer.
    """
    result = analyze_resume(sample_resume_text)
    print(result)
    print(result.model_dump())