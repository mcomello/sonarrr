import requests


def get_a_page(url):
    return requests.get(url).text


print(get_a_page('http://www.apple.com'))
