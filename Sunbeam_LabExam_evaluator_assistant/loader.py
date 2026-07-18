import os
import shutil
import zipfile
import json
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader

load_dotenv()

def load_marking_scheme(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def load_question_paper(pdf_path):
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    text = ""

    for doc in docs:
        text += doc.page_content + "\n"

    return text


def extract_submission(zip_path, output_folder="temp_submission"):

    if os.path.exists(output_folder):
        shutil.rmtree(output_folder)

    os.makedirs(output_folder)

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(output_folder)

    return output_folder


SUPPORTED = tuple(
    ext.strip()
    for ext in os.getenv(
        "SUPPORTED_EXTENSIONS",
        ".java,.py,.cpp,.c,.txt,.md"
    ).split(",")
)


def read_source_code(folder):

    code = ""

    for root, _, files in os.walk(folder):

        for file in files:

            if file.endswith(SUPPORTED):

                path = os.path.join(root, file)

                try:
                    with open(path, "r", encoding="utf-8") as f:

                        code += f"\n\n========== {file} ==========\n\n"

                        code += f.read()

                except Exception as e:
                    print(e)

    return code


def prepare_input(question_pdf, submission_zip):

    question = load_question_paper(question_pdf)

    folder = extract_submission(submission_zip)

    code = read_source_code(folder)

    return question, code