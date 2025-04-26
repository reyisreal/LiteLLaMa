from litellm import completion

response = completion(
    
    # enter the desired model name here, e.g., "llama2-7b-chat" or "llama2-13b-chat"
    # model="ollama/[MODEL_NAME]", 
    
    #enter the desired prompt here, e.g., "What is the capital of France?"
    # messages=[{ "content": "[prompt]","role": "user"}], 
    api_base="http://localhost:11434"
)
print(response["choices"][0]["message"]["content"])