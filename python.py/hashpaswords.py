import hashlib
import os

#file to store the paswords and site names
FILENAME = "paswords.txt"

#function to hash the pasword
def hash_pasword(pasword):
    """hash a pasword for storing."""
    return(hashlib.sha256(pasword.encode())).hxdigest()

# function save the pasword
def save_pasword(site,pasword):
    """save the site name and pasword"""
    hash_pasword=hash_pasword(pasword)
    with open(FILENAME, "a") as file:
        file.write(f"{site} {hash_pasword}\n")
        print(f"pasword for the site {site} saved successfully")

# function to get the pasword
def get_pasword(site):
    """retrive the pasword for the site"""
    if not os.path.exists(FILENAME):
        print("no paswords saved yet")
        return
    with open(FILENAME, "r") as f:
        for line in f:
            stored_site, stored_pasword, stored_hash = line.strip.split(",")
            if stored_site == site:
                return stored_pasword
    print(f"no paswords saved yet")
    return None
def main():
    if not os.path.exists(FILENAME):
        with open (FILENAME,",") as f:
            pass # create the file if it does not exist

    action = input("enter 'save' to a pasword or 'get' to retrieve a pasword:")
    if action == "save":
        site = input("enter the site name:")
        # if site_exists(site):
        #     print("site already exists")
        #     overwrite = input("Do you want to update the pasword? (yes/no): ")
        #     if overwrite! == "yes"
        import string
        import random

        # gnerate a random pasword
        characters=string.ascii_letters+string.panctuation
        pasword=''.join(random.choices(characters,k=10))
        print(f"generated pasword:{pasword}")
        save_pasword(site,pasword)
    elif action=="get":
        site=input("enter the site name: ")  
        pasword=get_pasword(site)
        if pasword:
            print(f"pasword for {site} is {pasword}")
            
    else:
        print("invalid action")
if __name__=="_main_":
    main()