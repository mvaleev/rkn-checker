#!/usr/bin/python3

import requests

dump_url = 'https://raw.githubusercontent.com/zapret-info/z-i/refs/heads/master/dump.csv'
destination = 'dump.csv'

def download_file(url, destination):
    response = requests.get(url)
    if response.status_code == 200:
        with open(destination, 'wb') as file:
            file.write(response.content)
        print(f'Saved as {destination}')
    else:
        print(f'Download error: {response.status_code}')


download_file(dump_url, destination)

