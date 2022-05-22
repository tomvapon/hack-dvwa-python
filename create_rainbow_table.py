from Crypto.Hash import MD5
import pickle


rainbow_dictionary = dict()
with open('rockyou.txt', 'rb') as unhash_passwords:
    for unhash_password in unhash_passwords:
        strip_unhash_password = unhash_password.strip(b'\n')
        rainbow_dictionary[MD5.new(strip_unhash_password).hexdigest()] = unhash_password

    # Save dictionary to file
    rainbow_file = open("rainbow_table.pkl", "wb")
    pickle.dump(rainbow_dictionary, rainbow_file)
    rainbow_file.close()
