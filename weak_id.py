import requests


# Target url for injection
target_url = 'http://localhost//vulnerabilities/weak_id/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'
}
cookies = {
    'dvwaSession':'1',
    'PHPSESSID': 'vv0uk98969asiqa2d79gcubn12',
    'security': 'low'
}

r = requests.get(target_url, headers=headers, cookies=cookies)
print(r.url)