from bs4 import BeautifulSoup as bs
import re
import requests


# Target URL
login_url = 'http://localhost/login.php'

# For the next attacks, it is supposed, the admin/password is
# already hacked with dictionary_attack_login.py
payload = {
    'username': 'admin',
    'password': 'password',
    'Login': 'Login'
}

# Open a new session to extract the links (possible targets)
with requests.Session() as session:
    # Get the login url
    r = session.get(login_url)

    # Extract user token
    token = re.search("user_token'\s*value='(.*?)'", r.text).group(1)
    payload['user_token'] = token

    # Login in the webpage
    p = session.post(login_url, data=payload)

    # Parse request p into tree
    tree = bs(p.text, 'html.parser')

    # Find all a anchor elements
    for link in tree.find_all('a'):
        print(f"{link.get('href')} -> {link.text}")