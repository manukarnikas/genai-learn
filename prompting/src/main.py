import os
from llama_index.core import PromptTemplate
from llama_index.llms.ollama import Ollama

llm = Ollama(
    model="tinyllama:latest",
    temperature=0.0
)

# template
template_str = (
    "You are an expert AI assistant.\n"
    "Use ONLY the use provided context to answer the user's question. "
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
template = PromptTemplate(template_str)

#sample
sample_context = (
    "NASA’s Artemis program aims to return humans to the Moon by the mid-2020s. "
    "Artemis I was an uncrewed test flight in 2022, successfully orbiting the Moon. "
    "Artemis II, scheduled for 2025, will carry astronauts on a lunar flyby. "
    "Artemis III, planned for 2026, aims to land the first woman and next man on the lunar surface. "
    "The program also intends to establish a sustainable presence by building a lunar Gateway space station "
    "and using the Moon as a stepping stone to Mars."
)
sample_query = "What are the main goals of the Artemis program?"

#usage
filled_prompt = template.format(
    context_str=sample_context,
    query_str=sample_query
)

#print
print(filled_prompt)

#response
response = llm.complete(prompt=filled_prompt)
print(response.text)