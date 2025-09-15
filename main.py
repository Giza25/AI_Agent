import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    model = "gemini-2.0-flash-001"
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
        )
    if verbose:
        print("User prompt:", user_prompt, '\n')
    print(response.text, '\n')
    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)


if __name__ == "__main__":
    main()
