import gradio as gr
import requests

API_URL = "http://127.0.0.1:8000/api/analyze"

def run_assistant(resume_query, job_query):
    payload = {
        "resume_query": resume_query,
        "job_query": job_query
    }

    try:
        response = requests.post(API_URL, json=payload)

        if response.status_code != 200:
            return {
                "error": f"Backend error {response.status_code}",
                "details": response.text
            }

        return response.json()

    except Exception as e:
        return {
            "error": "Failed to connect to backend",
            "details": str(e)
        }

with gr.Blocks(title="Agentic Job Assistant") as demo:
    gr.Markdown("## 🤖 Agentic Job Assistant")

    resume_query = gr.Textbox(label="Resume Search Query")
    job_query = gr.Textbox(label="Job Description Query")

    submit = gr.Button("Analyze")
    output = gr.JSON(label="Result")

    submit.click(
        run_assistant,
        inputs=[resume_query, job_query],
        outputs=output
    )

demo.launch()