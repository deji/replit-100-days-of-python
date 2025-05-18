import requests
import os


def get_news(country):
  newsKey = os.environ['NEWSAPI_KEY']
  country = country

  url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={newsKey}"

  result = requests.get(url)
  data = result.json()

  return data
