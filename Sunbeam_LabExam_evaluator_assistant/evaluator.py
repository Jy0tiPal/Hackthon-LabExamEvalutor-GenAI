import os
import json
import re

from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

# Initialize Groq LLM
llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model=os.getenv("MODEL_NAME", "llama-3.3-70b-versatile"),
    temperature=0
)

PROMPT = """
You are an experienced Java Lab Exam Evaluator.

Question Paper
---------------
{question}

Official Marking Scheme
-----------------------
{marking_scheme}

Student Source Code
-------------------
{code}

Instructions:

1. Evaluate ONLY according to the supplied marking scheme.
2. Use EXACT section names from the marking scheme.
3. DO NOT create new sections.
4. DO NOT remove any sections.
5. DO NOT change maximum marks.
6. Award partial marks whenever appropriate.
7. Return ONLY valid JSON.

Return JSON in this format:

{{
    "evaluation":[
        {{
            "section":"",
            "marks_awarded":0,
            "evidence":"",
            "evaluator_comments":""
        }}
    ],
    "overall_comment":""
}}
"""


def clean_json(text: str) -> str:
    """
    Extract only the JSON object from the LLM response.
    """

    # Remove markdown code fences
    text = re.sub(r"```json", "", text, flags=re.IGNORECASE)
    text = re.sub(r"```", "", text)

    # Find first JSON object
    match = re.search(r"\{.*\}", text, re.DOTALL)

    if match:
        return match.group(0).strip()

    raise ValueError("No JSON found in LLM response.")


def evaluate(question: str, code: str, marking_scheme):

    prompt = PROMPT.format(
        question=question,
        code=code,
        marking_scheme=json.dumps(
            marking_scheme,
            indent=4
        )
    )

    response = llm.invoke(prompt)

    result = clean_json(response.content)

    try:
        return json.loads(result)

    except Exception:
        print("\n===== LLM OUTPUT =====\n")
        print(result)
        raise