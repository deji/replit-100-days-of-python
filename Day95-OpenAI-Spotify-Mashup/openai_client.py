import os
from openai import OpenAI

def get_openai_client():
    """Initialize and return the OpenAI client"""
    return OpenAI(
        api_key=os.environ['OPENAPI_KEY'],
        organization=os.environ['ORGANISATION_ID']
    )

def summarize_news(client, title, description, temperature=0.8, max_tokens=20):
    """Summarize a news story in 2-3 words using OpenAI"""
    prompt = f"Summarize this news story in exactly 2-3 words that would make good song search terms. Story title: {title}. Story description: {description}"
    system_prompt = "You are a helpful assistant that summarizes news stories in exactly 2-3 words. Be creative but relevant. These words will be used to search for music, so make them emotional and evocative. Only respond with the 2-3 words, nothing else."

    response = client.responses.create(
        model="gpt-4.1-nano-2025-04-14",
        instructions=system_prompt,
        input=prompt,
        temperature=temperature,
        max_output_tokens=max_tokens
    )

    return response.output_text