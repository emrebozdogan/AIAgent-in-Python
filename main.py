import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.system_prompt import system_prompt
from call_function import available_functions, call_function
from functions.config import MAX_ITERS


def main():
    load_dotenv()
    
    args = sys.argv[1:]
    
    if not args:
        print("No prompt provided")
        sys.exit(1)

    verbose = False
    prompt_parts = []
    for arg in args:
        if arg == "--verbose":
            verbose = True
        else:
            prompt_parts.append(arg)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    

    if not prompt_parts:
        print("No prompt provided")
        sys.exit(1)

    user_prompt = " ".join(prompt_parts)
    
    if verbose:
        print(f"User prompt: {user_prompt}")

    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]
    
    for i in range(MAX_ITERS):
        try:
            result = generate_content_func(client, messages, verbose)
            if result:
                print(f"Response: {result}")
                break
        except Exception as e:
            print(f"Error: {e}")
            continue
    else:
        print("Max retries reached, no final response.")

def generate_content_func(client, messages, verbose):
    GenerateContentResponse = client.models.generate_content(
        model="gemini-2.0-flash-001",
         contents=messages,
         config=types.GenerateContentConfig(
            tools=[available_functions],
             system_instruction=system_prompt))


    if verbose:
        print(f"Prompt tokens: {GenerateContentResponse.usage_metadata.prompt_token_count}\nResponse tokens: {GenerateContentResponse.usage_metadata.candidates_token_count}")
        
    if GenerateContentResponse.candidates:
        for candidate in GenerateContentResponse.candidates:
            function_call_content = candidate.content
            messages.append(function_call_content)
    
    if not GenerateContentResponse.candidates:
        return GenerateContentResponse.text
    
    if GenerateContentResponse.function_calls:
        function_responses = []
        for function_call_part in GenerateContentResponse.function_calls:
            result_function_call = call_function(function_call_part, verbose)
            if not result_function_call.parts or \
               not hasattr(result_function_call.parts[0], 'function_response') or \
               result_function_call.parts[0].function_response is None:
                raise Exception(f"Error calling function: {function_call_part.name}. Function response not found or invalid.")
            
            if verbose:
                print(f"-> {result_function_call.parts[0].function_response.response}")

            function_responses.append(result_function_call.parts[0])

        messages.append(types.Content(role="user", parts=function_responses))

        return None

    else:
        return GenerateContentResponse.text
    



if __name__ == "__main__":
    main()
