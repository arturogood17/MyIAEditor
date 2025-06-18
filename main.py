import os
import sys
from system_prompt import system_prompt
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()
    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]
    if not args:
        print("No prompt was provided")
        print("Usage: python main.py 'prompt' [--verbose]")
        sys.exit(1)
    args = " ".join(args)

    messages = [types.Content(role="user", parts=[types.Part(text=args)]),]

    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key= api_key)
    
    response = generate_response(messages, client)
    
    if verbose:
        print("User prompt:", args)
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:",response.usage_metadata.candidates_token_count)
    print(response.text)

def generate_response(messages, client):
        response = client.models.generate_content(
        model= "gemini-2.0-flash-001", contents = messages,
        config= types.GenerateContentConfig(system_instruction= system_prompt))
        return response


if __name__ == "__main__":
    main()