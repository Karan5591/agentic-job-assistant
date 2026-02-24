from app.agents.resume_analyzer import analyze_resume

if __name__ == "__main__":
    sample_resume_text = """
    - Data Analyst with 4 years of experience.
    - Skilled in Python, SQL, Excel, Pandas.
    - Worked at ABC Corp as a Data Analyst.
    """
    result = analyze_resume(sample_resume_text)
    print(result)
    print(result.model_dump())