import os
from openai import OpenAI

default_model = "gpt-4.1-nano-2025-04-14"

def call_openai(client=None,
                model=default_model,
                user_prompt="",
                system_prompt="",
                temperature=0,
                max_output_tokens=100,
                debug=False):
    # Check if the client is None
    if client is None:
        print("Please provide a client")
        exit(1)

    # Check if the user prompt is empty
    if user_prompt == "" or system_prompt == "":
        print("Please provide a user prompt and a system prompt")
        exit(1)

    # Create a response using the Responses API
    response = client.responses.create(model=default_model,
                                       instructions=system_prompt,
                                       input=user_prompt,
                                       temperature=temperature,
                                       max_output_tokens=max_output_tokens)

    if debug:
        print(response.model_dump_json(indent=2))
        print("**********************************")

    # Print the response content
    print(response.output_text)

if __name__ == "__main__":

    # Initialize the client with API key and organization
    client = OpenAI(api_key=os.environ['OPENAPI_KEY'],
                    organization=os.environ['ORGANISATION_ID'])

    with open('prompt.txt', 'r') as file:
        prompt = file.read()

    with open('system.txt', 'r') as file:
        system_prompt = file.read()

    with open('site-available.txt', 'r') as file:
        site_available = file.read()

    with open('site-unavailable.txt', 'r') as file:
        site_unavailable = file.read()

    with open('site-available-sale.txt', 'r') as file:
        site_available_sale = file.read()

    # Call the function with the user prompt and system prompt
    user_prompt_available = f"{prompt}\n{site_available}"
    user_prompt_unavailable = f"{prompt}\n{site_unavailable}"
    user_prompt_available_sale = f"{prompt}\n{site_available_sale}"

    print("========== Calling OpenAI with site available prompt:")
    call_openai(client=client,
                user_prompt=user_prompt_available,
                system_prompt=system_prompt,
                max_output_tokens=50000)
    print()

    print("========== Calling OpenAI with site unavailable prompt:")
    call_openai(client=client,
                user_prompt=user_prompt_unavailable,
                system_prompt=system_prompt,
                max_output_tokens=50000)
    print()

    print("========== Calling OpenAI with site available sales prompt:")
    call_openai(client=client,
                user_prompt=user_prompt_available_sale,
                system_prompt=system_prompt,
                max_output_tokens=50000)
