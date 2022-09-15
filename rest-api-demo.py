import requests

NYT_ARTICLE_SEARCH_API_BASE_URL = 'https://api.nytimes.com/svc/search/v2/articlesearch.json'
NYT_ARTICLE_SEARCH_API_KEY = 'zBUKdYxLkvd8g0A8cZpgUxz1Z8bNapkj'

response = requests.get(
    NYT_ARTICLE_SEARCH_API_BASE_URL,
     params={
        'q': 'Texas State University',
        'api-key': NYT_ARTICLE_SEARCH_API_KEY
     }
)

print(response)