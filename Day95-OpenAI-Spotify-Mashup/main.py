import os

from news import get_news
from spotify_client import get_spotify_client, search_track
from openai_client import get_openai_client, summarize_news

def main():
    # Initialize clients
    openai_client = get_openai_client()
    spotify_client = get_spotify_client()

    # Get news stories
    news = get_news("us")
    if not (news['status'] == 'ok' and news['totalResults'] > 0):
        print("No news found")
        exit(1)

    # Process up to 5 top stories
    stories = news['articles'][:5]
    for story in stories:
        title = story['title']
        description = story['description']

        print(f"\nProcessing story: {title}")

        # Get song search terms from OpenAI
        summary = summarize_news(openai_client, title, description)
        print(f"Search terms: {summary}")

        # Search for a matching track
        track = search_track(spotify_client, summary)
        if track:
            print(f"Track found: {track['name']} by {track['artist']}")
            print(f"Preview URL: {track['preview_url']}")
            print(f"Listen on Spotify: {track['spotify_url']}")
        else:
            print("No track found for these search terms")

        print("-" * 50)

if __name__ == "__main__":
    main()