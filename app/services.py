import ollama
import re

MODEL_NAME = "llama3.2"

def code_explainer(code: str) -> dict:
    """
    Send code to LLM and return explanation, diagram, and summary separately.
    """
    prompt = f"""
        You are a helpful code explainer.
        Given the following code, provide output in this exact format:

        ### Explanation
        (step by step explanation)

        ### Diagram
        (Mermaid diagram only, inside a code block. Rules:
        - Start with 'graph LR'
        - Use only '-->' for arrows
        - Arrow labels must be written like: A -->|label| B
        - Do NOT add extra characters like '>' after labels
        - Do not include any text outside the diagram code block)

        ### Summary
        (2–3 sentences)

        Code:
        {code}
        """


    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are an expert software explainer."},
            {"role": "user", "content": prompt}
        ],
    )

    content = response["message"]["content"]

    # Extract sections
    explanation = extract_section(content, "Explanation")
    diagram = clean_mermaid(extract_section(content, "Diagram"))
    summary = extract_section(content, "Summary")

    print(f'{diagram = }')
    return {
        "explanation": explanation.strip(),
        "diagram": diagram.strip(),
        "summary": summary.strip()
    }


def extract_section(text: str, section: str) -> str:
    """
    Extract a section by header (### SectionName).
    """
    pattern = rf"### {section}\n([\s\S]*?)(?=###|\Z)"
    match = re.search(pattern, text)
    return match.group(1).strip() if match else ""


def clean_mermaid(diagram: str) -> str:
    """
    Remove ```mermaid fences and fix common syntax issues.
    """
    text = diagram.replace("```mermaid", "").replace("```", "").strip()
    # Fix common mistake: |label|>
    text = re.sub(r"\|\s*([^|]+?)\s*\|>", r"|\1|", text)
    return text
