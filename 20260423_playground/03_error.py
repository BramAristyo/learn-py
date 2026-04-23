def generate_ai_response(prompt):
    print(f"Processing prompt: '{prompt}'...")

    try:
        if prompt == "":
            raise ValueError("Prompt cannot be empty!")
        elif prompt == "error":
            raise Exception("error!")
        return "This is the generated answer from the LLM."
    except ValueError as e:
        return f"Validation Error: {e}"
    except Exception as e:
        return f"Internal server Error: {e}"


print(generate_ai_response("What is RAG?"))
print(generate_ai_response(""))  # This will trigger the ValueError
print(generate_ai_response("error"))  # This will trigger the Exception
