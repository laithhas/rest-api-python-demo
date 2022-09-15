import requests
import json

NYT_ARTICLE_SEARCH_API_BASE_URL = 'https://api.nytimes.com/svc/search/v2/articlesearch.json'
NYT_ARTICLE_SEARCH_API_KEY = 'zBUKdYxLkvd8g0A8cZpgUxz1Z8bNapkj'

response = requests.get(
    NYT_ARTICLE_SEARCH_API_BASE_URL,
     params={
        'q': 'Texas State University',
        'api-key': NYT_ARTICLE_SEARCH_API_KEY
     }
)

json_data = response.json()
pretty_json_data = json.dumps(json_data, indent=4, sort_keys=True)

print(pretty_json_data)