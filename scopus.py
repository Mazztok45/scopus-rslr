import requests
import json
import os

# Replace with your actual API key and desired query
api_key = os.environ["SCOPUS_API_KEY"] # Use secrets for production!
query = 'TITLE("FAIR" AND "research software")'  # Replace with your search query

# Base URL for the Scopus Search API
base_url = "https://api.elsevier.com/content/search/scopus"

# Parameters for the API request
params = {
    "query": query,
    "apiKey": api_key,
    "count": 25,  # Number of results per page (max 25)
    "start": 0    # Starting index for results
}

# Make the API request
try:
    response = requests.get(base_url, params=params, headers={'Accept': 'application/json'})
    response.raise_for_status()  # Raise an exception for bad status codes

    # Parse the JSON response
    data = response.json()

    # Process the results
    if 'search-results' in data and 'entry' in data['search-results']:
        articles = data['search-results']['entry']
        print(f"Found {len(articles)} articles for query: '{query}'")
        for i, article in enumerate(articles):
            title = article.get('dc:title', 'No Title')
            creator = article.get('dc:creator', 'No Creator')
            publication_name = article.get('prism:publicationName', 'No Publication Name')
            cover_date = article.get('prism:coverDate', 'No Date')
            doi = article.get('prism:doi', 'No DOI')

            print(f"\nArticle {i+1}:")
            print(f"  Title: {title}")
            print(f"  Creator: {creator}")
            print(f"  Publication: {publication_name}")
            print(f"  Date: {cover_date}")
            print(f"  DOI: {doi}")

    else:
        print("No search results found.")
        print("Full response:")
        print(json.dumps(data, indent=2))

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
    if response is not None:
        print(f"Response status code: {response.status_code}")
        print(f"Response text: {response.text}")
