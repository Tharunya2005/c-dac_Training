"""
An example to get data from a REST server using `requests` library
"""

import requests


if __name__ == '__main__':
    api_key = 'aa9e49f'
    search_text = input('What do you want to search? ')
    url = f'https://omdbapi.com/?s={search_text}&apikey={api_key}'
    r = requests.get(url)

    if r.status_code != 200:
        print('Something wrong. Please try again.')
        exit(1)

    data = r.json()
    print(f'Found {data["totalResults"]} movies/shows')
    movies = data['Search']
    for i, m in enumerate(movies):
        print(f'{i+1}. {m["Title"]} ({m["Year"]})')