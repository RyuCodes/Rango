import json
import urllib.parse
import urllib.request
import urllib.error

# Downloaded python package
import requests

# For errors
import base64

def run_query(search_terms):
    # specify base
    root_url = 'https://api.cognitive.microsoft.com/bing/v7.0/search/'

    # specify how many results returned per pages
    # Offset specifies where in results list to start from
    results_per_page = 10
    offset = 0

    headers = {
    # Request headers
        'Ocp-Apim-Subscription-Key': 'cf39f72e278e47dc81f7ec57ed228b37',
    }

    #constructs request URL
    params = urllib.parse.urlencode({
    # Request parameters; specified by bing
        'q': search_terms,
        'count': results_per_page,
        'offset': offset,
        'mkt': 'en-us',
    })


    # Create results list
    results = []

    try:
        # uses downloaded requests function, which will pass the unicode back
        # can use the internal decoder to get json (.json())
        response = requests.get(root_url, headers=headers, params=params)

        # will raise an http_error if not 200, which will punt this to the except portion
        response.raise_for_status()
        json_response = response.json()

        # Loop through each page returned, populating results list
        for result in json_response['webPages']['value']:
            results.append({
                'title': result['name'],
                'link': result['url'],
                'summary': result['snippet']
            })

    except Exception as e:
        print("Error when querying the Bing API: ", e)

    return results

if __name__ == '__main__':
    query = input("Enter Search Terms: ")
    results = run_query(query)

    for result in results:
        print("Title: {0}, Link: {1}".format(result['title'], result['link']))
