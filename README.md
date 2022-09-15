# rest-api-python-demo

This demo shows how to call the New York Times API using the Python requests library and parse its JSON data.

It also shows how you can store and hide your API keys with a `.env` file and `.gitignore` file, respectively.

## Part 1 — Get article headlines for topic
1. Check out NYT API
2. Create app using NYT Dev console: https://developer.nytimes.com/my-apps
3. Get API key for sending requests
4. `pip install requests`
5. Write initial article search request code
6. Read JSON from response
7. Print JSON into a nicer format
8. Get article headlines from JSON

## Part 2 — Hide API Key
1. `import os`
2. `pip install python-dotenv`
3. Create `.env` file and add key to `NYT_KEY` variable
4. Get `NYT_KEY` from environment variable using dotenv
5. Create `.gitignore` and add `.env` to it
