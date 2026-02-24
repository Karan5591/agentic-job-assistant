from app.orchestrator.job_assistant import run_job_assistant
import json

if __name__ == "__main__":
    result = run_job_assistant(
        resume_query="Python developer with SQL experience",
        job_query="Looking for a Python and SQL backend developer"
    )

    print(json.dumps(result, indent=2))