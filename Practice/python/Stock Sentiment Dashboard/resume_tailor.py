import openai
from fpdf import FPDF
import argparse
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def tailor_resume(job_description, resume_text):
    prompt = f"""
    You are a professional resume writer.
    Given the following job description and resume, tailor the resume to match the job, emphasizing relevant skills:

    JOB DESCRIPTION:
    {job_description}

    ORIGINAL RESUME:
    {resume_text}

    TAILORED RESUME:
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
    )
    return response['choices'][0]['message']['content']

def save_pdf(text, filename="tailored_resume.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    for line in text.split('\n'):
        pdf.multi_cell(0, 10, line)

    pdf.output(filename)
    print(f"📄 Resume saved as {filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--job', required=True, help="Path to job description text file")
    parser.add_argument('--resume', required=True, help="Path to resume text file")
    args = parser.parse_args()

    with open(args.job, 'r') as job_file:
        job_desc = job_file.read()

    with open(args.resume, 'r') as resume_file:
        resume_text = resume_file.read()

    result = tailor_resume(job_desc, resume_text)
    save_pdf(result)
