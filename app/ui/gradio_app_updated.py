import gradio as gr
import requests

API_URL = "http://127.0.0.1:8000/api/screen"


def screen_candidates_ui(job_description, resumes, top_n):
    if job_description is None or not resumes:
        return {"error": "Please upload a job description and at least one resume"}

    files = []

    # Job description
    files.append(
        (
            "job_description",
            (job_description.name, open(job_description.name, "rb")),
        )
    )

    # Multiple resumes
    for resume in resumes:
        files.append(
            (
                "resumes",
                (resume.name, open(resume.name, "rb")),
            )
        )

    data = {
        "top_n": str(top_n),
    }

    try:
        response = requests.post(API_URL, files=files, data=data)

        if response.status_code != 200:
            return {
                "error": f"Backend error {response.status_code}",
                "details": response.text,
            }

        return response.json()

    except Exception as e:
        return {
            "error": "Failed to connect to backend",
            "details": str(e),
        }


with gr.Blocks(title="Recruiter Resume Screening") as demo:
    gr.Markdown("## 🤖 Recruiter Resume Screening System")
    gr.Markdown(
        "Upload a job description and multiple resumes to get the top matching candidates."
    )

    with gr.Row():
        job_description = gr.File(
            label="Upload Job Description (PDF/DOCX)",
            file_types=[".pdf", ".docx"],
        )

    with gr.Row():
        resumes = gr.File(
            label="Upload Resumes (Multiple)",
            file_types=[".pdf", ".docx"],
            file_count="multiple",
        )

    top_n = gr.Slider(
        minimum=1,
        maximum=20,
        step=1,
        value=5,
        label="Number of Top Candidates",
    )

    submit_btn = gr.Button("🔍 Screen Candidates")

    output = gr.JSON(label="Screening Results")

    submit_btn.click(
        fn=screen_candidates_ui,
        inputs=[job_description, resumes, top_n],
        outputs=output,
    )

demo.launch()