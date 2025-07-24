import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from call_function import available_functions

def main():
    load_dotenv()

    system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    # My original code
    # if len(sys.argv) == 1:
    #     print("Error: No prompt entered.")
    #     sys.exit(1)

    #Boot.Dev's code, which I like better
    args = sys.argv[1:]

    if not args:
        print("AI Code Assistant")
        print('\nUsage: uv run main.py "your prompt here"')
        print('Example: uv run main.py "How do I build a calculator app?"')
        sys.exit(1)
    # user_prompt = " ".join(args)
    user_prompt = " ".join([arg for arg in args if not arg.startswith("--")])

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

    response = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt)
    )

    if not response.function_calls:
        print(response.text)
    for function_call_part in response.function_calls:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")

    if "--verbose" in args:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    

if __name__ == "__main__":
    main()
