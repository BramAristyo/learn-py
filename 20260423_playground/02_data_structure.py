ai_tools = ["LangChain", "ChromaDB", "StreamLit"]
ai_tools.append("Groq")

print("List of tools")
for tool in ai_tools:
    print(f"- {tool}")

llm_response = {
    "status": 200,
    "model": "Llama-3",
    "usage": {"prompt_tokens": 50, "completion_tokens": 800},
    "answer": "RAG is the future of enterprise AI",
}

tokens_used = llm_response["usage"]["completion_tokens"]
print(f"\nAI Answer: {llm_response['answer']}")
print(f"Tokens used: {tokens_used}")
