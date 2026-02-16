# --- ZERO-SHOT ---
import os
from llama_index.core import PromptTemplate
from llama_index.llms.openai import OpenAI

os.environ['OPENAI_API_KEY'] = 'ADD_SECRET_KEY'

def run_llm_zeroshot(context: str, query: str) -> str:
  
    llm = OpenAI(
        model="gpt-3.5-turbo",
        temperature=0
    )

    template_str = (
        "You are an expert AI assistant.\n"
        "Use ONLY use the provided context to answer the user's question. "
        "If the context is insufficient or does not mention the answer, reply exactly: "
        "'Not enough information.'\n\n"
        "Context:\n{context_str}\n\n"
        "User Question: {query_str}\n\n"
        "Answering Rules:\n"
        "1) Be concise and precise (3–6 sentences, unless the question requires more).\n"
        "2) Use bullet points for lists.\n"
        "3) At the end, include a 'Sources:' section with short snippets or filenames from the context you used.\n\n"
        "Final Answer:"
    )
    prompt = PromptTemplate(template_str).format(context_str=context, query_str=query)
    response = llm.complete(prompt=prompt)
    output = response.text
    return output

# Zero-Shot: No examples, just context + query
context_text = (
    "Volleyball is know as Haikyu is Japan and is a very popular sport"
    "Along with good technique, Vertical Jump is a skill that allows a spiker to be effective and destroy blocks"
)

query_text = "What is an important skill for a spiker?"

ans = run_llm_zeroshot(context=context_text, query=query_text)

print(ans)