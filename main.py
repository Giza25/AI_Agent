import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
import prompts
import call_function

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("API key was not found")

    client = genai.Client(api_key=api_key)

    model = "gemini-2.5-flash"
    if len(sys.argv) > 1:
        user_prompt = sys.argv[1]
    else:
        print("Put a prompt after the name of the script!")
        return 1
    
    verbose = False
    if len(sys.argv) > 2:
        if sys.argv[2] == "--verbose":
            verbose = True
    
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

    response = client.models.generate_content(
        model=model, 
        contents=messages,
        config=types.GenerateContentConfig(
            system_instruction=prompts.system_prompt, 
            tools=[call_function.available_functions]
            )
        )
    
    called_count = 0
    if response.function_calls is not None:
        function_call = response.function_calls
        called_count = len(function_call)

    if verbose:
        print("User prompt:", user_prompt, '\n')
    if response.function_calls is not None:
        for i in range(called_count):
            print(f"Calling function: {function_call[i].name}({function_call[i].args})")
    else:
        print(response.text, '\n')
    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)


if __name__ == "__main__":
    main()
