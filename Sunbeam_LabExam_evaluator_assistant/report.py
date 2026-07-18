import os
import json


def apply_marking_scheme(result, marking_scheme):
    """
    Apply official marking scheme to AI evaluation.
    """

    # AI response indexed by section name
    ai_sections = {
        item["section"]: item
        for item in result["evaluation"]
    }

    evaluation = []
    total = 0

    for section in marking_scheme["sections"]:

        name = section["section"]
        max_marks = section["maximum_marks"]

        if name in ai_sections:

            ai_item = ai_sections[name]

            awarded = min(
                ai_item.get("marks_awarded", 0),
                max_marks
            )

            evaluation.append({
                "section": name,
                "marks_awarded": awarded,
                "maximum_marks": max_marks,
                "evidence": ai_item.get("evidence", ""),
                "evaluator_comments": ai_item.get(
                    "evaluator_comments",
                    ""
                )
            })

            total += awarded

        else:

            evaluation.append({
                "section": name,
                "marks_awarded": 0,
                "maximum_marks": max_marks,
                "evidence": "Section not evaluated.",
                "evaluator_comments": "No evaluation returned by AI."
            })

    result["evaluation"] = evaluation
    result["total_marks"] = total
    result["maximum_marks"] = marking_scheme["total_marks"]

    return result


def calculate_totals(result, marking_scheme):
    """
    Recalculate total marks.
    """

    total = sum(
        item["marks_awarded"]
        for item in result["evaluation"]
    )

    result["total_marks"] = total
    result["maximum_marks"] = marking_scheme["total_marks"]

    return result


def generate_report(result):

    os.makedirs("reports", exist_ok=True)

    with open(
        "reports/evaluation_report.json",
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(result, f, indent=4)

    print("\n========== Evaluation Report ==========")
    print(f"Student ID : {result['student_id']}")
    print("=" * 70)

    for item in result["evaluation"]:

        print(f"Section   : {item['section']}")
        print(f"Marks     : {item['marks_awarded']}/{item['maximum_marks']}")
        print(f"Evidence  : {item['evidence']}")
        print(f"Comments  : {item['evaluator_comments']}")
        print("-" * 70)

    print(
        f"TOTAL MARKS : "
        f"{result['total_marks']}/{result['maximum_marks']}"
    )


def save_markdown_report(result):

    os.makedirs("reports", exist_ok=True)

    student_id = result["student_id"]

    filename = f"reports/{student_id}.md"

    total = result["total_marks"]
    max_total = result["maximum_marks"]

    percentage = (
        total / max_total * 100
        if max_total else 0
    )

    with open(filename, "w", encoding="utf-8") as f:

        f.write("# AI Lab Exam Evaluation Report\n\n")

        f.write(f"**Student ID:** {student_id}\n\n")

        f.write(
            f"**Total Marks:** **{total}/{max_total}**\n\n"
        )

        f.write(
            f"**Percentage:** **{percentage:.2f}%**\n\n"
        )

        f.write("---\n\n")

        f.write("## Section-wise Evaluation\n\n")

        f.write("| Section | Marks | Evidence | Evaluator Comments |\n")
        f.write("|---------|------:|----------|--------------------|\n")

        for item in result["evaluation"]:

            f.write(
                f"| {item['section']} | "
                f"{item['marks_awarded']}/{item['maximum_marks']} | "
                f"{item['evidence']} | "
                f"{item['evaluator_comments']} |\n"
            )

        f.write("\n---\n\n")

        f.write("## Overall Feedback\n\n")

        f.write(
            result.get(
                "overall_comment",
                "No feedback available."
            )
        )

    print(f"\nMarkdown report saved: {filename}")