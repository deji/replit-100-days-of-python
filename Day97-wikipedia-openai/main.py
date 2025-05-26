import requests
from bs4 import BeautifulSoup

import my_openai


def parse_wiki_article(html_response):
    title, article, refs = None, None, None
    soup = BeautifulSoup(html_response, 'html.parser')

    title = soup.select_one('h1').text
    article = soup.select_one('div#bodyContent')
    if article:
        refs = soup.select('div.reflist')
    return title, article, refs


url = "https://en.wikipedia.org/wiki/Hair_loss"
keywords = ['python', 'replit']

headers = {
    'accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language':
    'en-GB,en;q=0.6',
    'sec-ch-ua':
    '"Chromium";v="136", "Brave";v="136", "Not.A/Brand";v="99"',
    'sec-ch-ua-mobile':
    '?0',
    'sec-ch-ua-platform':
    '"Linux"',
    'sec-fetch-dest':
    'document',
    'sec-fetch-mode':
    'navigate',
    'sec-fetch-site':
    'same-origin',
    'sec-fetch-user':
    '?1',
    'sec-gpc':
    '1',
    'user-agent':
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'
}

system_prompt = "You're a helpful assistant with expertise in summarising Wikipedia articles. Use a simple language understandable to a 10 year old and don't use any jargon."

if __name__ == "__main__":
    response = requests.get(url, headers=headers)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    title, article, reflist = parse_wiki_article(html)

    user_prompt = f"Summarise the following Wikipedia article in no more than three paragraphs and in under 500 words.\n\n{article}\n"

    summary = my_openai.call_openai(client=my_openai.client,
                                    user_prompt=user_prompt,
                                    system_prompt=system_prompt,
                                    max_output_tokens=5000)

    print(title)
    print("=" * len(title))
    print(summary)

    print()
    print("References")
    print("-" * len("References"))

    for refs in reflist:
        for ref in refs.find_all('cite', class_='citation'):
            print(f"* {ref.text}")
            print()
