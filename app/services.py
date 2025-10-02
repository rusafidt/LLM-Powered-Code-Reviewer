import os
import re
from huggingface_hub import InferenceClient

# --- Config ---
MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.2"
HF_TOKEN = os.getenv("HF_TOKEN")  # set once:  $env:HF_TOKEN="hf_XXXX"

# Create a single client (reuse across calls)
_client = InferenceClient(token=HF_TOKEN)

def code_explainer(code: str) -> dict:
    """
    Send code to a hosted Hugging Face chat model and return
    explanation, diagram, and summary separately.
    """
    prompt = f"""
You are a helpful code explainer.
Given the following code, provide output in this exact format:

### Explanation
(step by step explanation)

### Summary
(2–3 sentences)

Code:
{code}
""".strip()

    # Call HF chat-completions (model is exposed as a chat model)
    resp = _client.chat_completion(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are an expert software explainer."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=2048,      # adjust as you like
        temperature=0.2,
    )

    content = resp.choices[0].message["content"]

    # Extract sections
    explanation = extract_section(content, "Explanation")
    summary = extract_section(content, "Summary")

    return {
        "explanation": explanation.strip(),
        "summary": summary.strip(),
    }

def extract_section(text: str, section: str) -> str:
    """Extract text between known section headers."""
    sections = ["Explanation", "Summary"]  # add "Diagram" here if you use it
    next_sections = [s for s in sections if s != section]

    start_pat = rf"###\s*{re.escape(section)}\s*\n"
    end_pat = r"\Z" if not next_sections else rf"(?=\n###\s*(?:{'|'.join(map(re.escape, next_sections))})\b|\Z)"

    m = re.search(start_pat + r"([\s\S]*?)" + end_pat, text)
    return m.group(1).strip() if m else ""

