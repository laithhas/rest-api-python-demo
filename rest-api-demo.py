import requests
import json
from os import getenv
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())  # This loads our .env file in this path

NYT_API_BASE_URL = "https://api.nytimes.com/svc/"
NYT_ARTICLE_SEARCH_PATH = "search/v2/articlesearch.json"
TXST_SEARCH_QUERY_PARAM = "Texas State University"
COCAINE_BEAR_QUERY_PARAM = "Cocaine Bear"

nyt_rest_api_response = requests.get(
    NYT_API_BASE_URL + NYT_ARTICLE_SEARCH_PATH,
    params={
        "q": TXST_SEARCH_QUERY_PARAM,
        "api-key": getenv("NYT_ARTICLE_SEARCH_API_KEY"),
    },
)

pretty_json_data = json.dumps(nyt_rest_api_response.json(), indent=4, sort_keys=True)
articles_list = nyt_rest_api_response.json()["response"]["docs"]

for i in range(10):
    print(articles_list[i]["headline"]["main"])
