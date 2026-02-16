# --- FEW-SHOT ---
import os
from typing import List, Dict
from llama_index.core import PromptTemplate
from llama_index.llms.openai import OpenAI

os.environ['OPENAI_API_KEY'] = 'ADD_SECRET_KEY'

def run_llm_fewshot(context: str, query: str, examples: List[Dict[str, str]]) -> str:
    llm = OpenAI(
        model="gpt-3.5-turbo",
        temperature=0
    )

    examples_str = "\n".join(
        f"Example {i+1}:\nContext:\n{ex.get('context','')}\n"
        f"Question: {ex.get('question','')}\n"
        f"Answer: {ex.get('answer','')}\n"
        for i, ex in enumerate(examples)
    )

    template_str = (
        "You are an expert AI assistant.\n"
        "Use ONLY the provided context to answer the user's question. "
        "If the context is insufficient or does not mention the answer, reply exactly: "
        "'Not enough information.'\n\n"
        "Follow the style and reasoning illustrated by the examples.\n\n"
        "Examples:\n{examples_str}\n"
        "--- End of Examples ---\n\n"
        "Context:\n{context_str}\n\n"
        "User Question: {query_str}\n\n"
        "Answering Rules:\n"
        "1) Be concise and precise (3–6 sentences, unless the question requires more).\n"
        "2) Use bullet points for lists.\n"
        "3) At the end, include a 'Sources:' section with short snippets or filenames from the context you used.\n\n"
        "Final Answer:"
    )

    prompt = PromptTemplate(template_str).format(
        examples_str=examples_str,
        context_str=context,
        query_str=query
    )

    return llm.complete(prompt=prompt).text


# Few-Shot: Fun examples
shots = [
    {
        "context": "Golden retrievers are friendly, intelligent dogs that require daily exercise and enjoy social interaction.",
        "question": "Why do golden retrievers need regular exercise?",
        "answer": (
            "They need exercise to stay healthy and mentally stimulated.\n"
            "- Prevents boredom and destructive behavior.\n"
            "- Maintains healthy weight and joint health.\n"
            "Sources: dog_care_guide.txt"
        )
    },
    {
        "context": "Wood-fired pizza ovens cook at extremely high temperatures, creating a crispy crust and smoky flavor.",
        "question": "What makes wood-fired pizza taste different?",
        "answer": (
            "The high heat and burning wood enhance flavor and texture.\n"
            "- Produces a crisp crust.\n"
            "- Adds a subtle smoky taste.\n"
            "Sources: pizza_handbook.pdf"
        )
    },
]

context_text = (
    "Context from gaming_basics.txt "
    "In cooperative multiplayer games, players work together to achieve a shared objective, "
    "often combining different character abilities to succeed."
)

query_text = "Why is teamwork important in cooperative multiplayer games?"

ans = run_llm_fewshot(context=context_text, query=query_text, examples=shots)

print(ans)
