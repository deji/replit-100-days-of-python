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

    return response.output_text


client = OpenAI(api_key=os.environ['OPENAPI_KEY'],
                organization=os.environ['ORGANISATION_ID'])
