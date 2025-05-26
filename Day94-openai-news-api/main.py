import requests
import json
import os
from openai import OpenAI

from news import get_news


def call_openai(client=None,
                model="gpt-4.1-nano-2025-04-14",
                user_prompt="",
                system_prompt="",
                temperature=0,
                max_output_tokens=16,
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
    response = client.responses.create(model="gpt-4.1-nano-2025-04-14",
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

    # Get the news
    news = get_news("us")
    if not (news['status'] == 'ok' and news['totalResults'] > 0):
        print("No news found")
        exit(1)

    # Initialize the client with API key and organization
    client = OpenAI(api_key=os.environ['OPENAPI_KEY'],
                    organization=os.environ['ORGANISATION_ID'])

    # Call the function with the user prompt and system prompt
    user_prompt = f"""{news} Use only this json for answering questions. Do not consult any other sources. You understand how to read the JSON format and can answer questions about the data it holds.

    First calculate the ranking of the sources based on their public prestige and reliability. Do not show the ranking but use it to order the summary of the news in each of the articles in the JSON using both the description and content where available. Do not show repeated articles. Instead show only the article with the highest score.

    Before each summary, include the title and source of the article. Do not include any other information. ENSURE that the summaries are in the order of the combined score of the public prestige, it's reliability and popularity of the news articles source.
    """
    system_prompt = "You are a helpful assistant with lots of experience in the news industry and a background in journalism. Provide only facts and no opinions. If you don't know the answer, say 'I don't know'."

    call_openai(client=client,
                user_prompt=user_prompt,
                system_prompt=system_prompt,
                max_output_tokens=50000)
