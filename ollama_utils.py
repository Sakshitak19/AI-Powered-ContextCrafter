import ollama

def generate_response(prompt, model='gemma3'):
    response = ollama.chat(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response['message']['content']
