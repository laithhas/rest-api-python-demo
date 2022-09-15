import requests
import json
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())  # This is to load your API keys from .env

NYT_ARTICLE_SEARCH_API_BASE_URL = 'https://api.nytimes.com/svc/search/v2/articlesearch.json'
NYT_ARTICLE_SEARCH_API_KEY = 'zBUKdYxLkvd8g0A8cZpgUxz1Z8bNapkj'

response = requests.get(
    NYT_ARTICLE_SEARCH_API_BASE_URL,
     params={
        'q': 'Texas State University',
        'api-key': os.getenv('NYT_ARTICLE_SEARCH_API_KEY')
     }
)

json_data = response.json()
pretty_json_data = json.dumps(json_data, indent=4, sort_keys=True)
print(pretty_json_data)

article_objects = json_data['response']['docs']

for article in article_objects:
    print(article['headline']['main'])