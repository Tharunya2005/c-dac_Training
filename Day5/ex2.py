"""
An example to get data from a REST server using `requests` library
"""

import requests


if __name__ == '__main__':
    url = f'https://vin-contact-service.onrender.com/api/contacts'
    r = requests.get(url)

    if r.status_code != 200:
        print('Something wrong. Please try again.')
        exit(1)


    data = r.json()
    print(f'Found {data["totalElements"]} records.')

    for i, m in enumerate(data["content"]):
        print(f'{i+1}. {m["firstname"]} {m["lastname"]}')