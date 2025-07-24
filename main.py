import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from call_function import available_functions, call_function
# from config import WOORKING_DIR
# from functions.call_function import call_function

def main():
    load_dotenv()

    system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.

If "run" shows up, I want you to execute a file.
"""

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    # My original code
    # if len(sys.argv) == 1:
    #     print("Error: No prompt entered.")
    #     sys.exit(1)

    #Boot.Dev's code, which I like better
    verbose = "--verbose" in sys.argv
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

    if "--verbose" in args:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    if not response.function_calls:
        print(response.text)

    function_responses = []
    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose)
        if (
            not function_call_result.parts
            or not function_call_result.parts[0].function_response
        ):
            raise Exception("empty function call result")
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
        function_responses.append(function_call_result.parts[0])

    if not function_responses:
        raise Exception("no function responses generated, exiting.")



if __name__ == "__main__":
    main()
