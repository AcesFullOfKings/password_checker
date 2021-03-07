import requests
import hashlib

while True:
    password = input("Enter a password: ")
    pw_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    hash_prefix = pw_hash[:5]
    hash_suffix = pw_hash[5:]

    page = requests.get("https://api.pwnedpasswords.com/range/{prefix}".format(prefix=hash_prefix)).text

    results = {line.split(":")[0] : line.split(":")[1] for line in page.split("\r\n") if line != ""}

    if hash_suffix in results:
        print("Password has been cracked! Number of times leaked: " + str(results[hash_suffix]))
    else:
        print("Password not found - it's probably not been leaked..")
