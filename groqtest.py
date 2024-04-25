import os
from llama_index.llms.groq import Groq

Groq.api_key = os.environ["GROQ_API_KEY"]
llm_groq = Groq("llama3-70b-8192")

response = llm_groq.complete("Explain the importance of low latency LLMs")
print(response)