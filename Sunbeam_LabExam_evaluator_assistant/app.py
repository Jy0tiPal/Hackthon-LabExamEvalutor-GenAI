import os
from dotenv import load_dotenv

from loader import prepare_input, load_marking_scheme
from evaluator import evaluate
from report import ( generate_report, save_markdown_report, calculate_totals, apply_marking_scheme)

marking_scheme = load_marking_scheme(
    os.getenv("MARKING_SCHEME_PATH")
)

load_dotenv()

print("=" * 60)
print("AI LAB EXAM EVALUATION ASSISTANT")
print("=" * 60)

student_id = input("Enter Student Roll No / PRN : ").strip()

solution_zip = input("Enter Student Solution ZIP Path : ").strip()

# Read question paper path from .env
question_pdf = os.getenv("QUESTION_PAPER_PATH")

if not question_pdf:
    raise ValueError("QUESTION_PAPER_PATH is not set in .env")

question, code = prepare_input(question_pdf, solution_zip)

result = evaluate(question, code, marking_scheme)

result["student_id"] = student_id
result = apply_marking_scheme(
    result,
    marking_scheme
)
result = calculate_totals(result, marking_scheme)


generate_report(result)
save_markdown_report(result)

print("\nEvaluation Completed Successfully.")
print("Report saved in reports/evaluation_report.json")