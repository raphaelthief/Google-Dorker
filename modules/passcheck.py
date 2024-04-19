import hashlib
import requests
from colorama import init, Fore, Style


def start():
    init()

def calculate_sha1(input_string):
    # Convert to SHA-1
    sha1_hash = hashlib.sha1(input_string.encode()).hexdigest()
    return sha1_hash

def call_api_with_sha1(sha1_hash):
    # Call API with hash SHA-1
    api_url = f"https://api.breachdirectory.org/passsearch?hash={sha1_hash}"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def checkit(word):
   
    # Convertir le mot en hash SHA-1
    sha1_hash = calculate_sha1(word)
    
    # Appeler l'API avec le hash SHA-1
    api_response = call_api_with_sha1(sha1_hash)
    
    if api_response:
        print(f"{Fore.RED}[+] {Fore.YELLOW}Password Check :{Fore.GREEN}")
        print(f"{Fore.YELLOW}API response (Password usage count) : {Fore.GREEN}", api_response)
    else:
        print(f"{Fore.RED}[Debug] Error API ...")


def checkit2(word):
   
    # Convertir le mot en hash SHA-1
    sha1_hash = calculate_sha1(word)
    
    # Appeler l'API avec le hash SHA-1
    api_response = call_api_with_sha1(sha1_hash)
    
    if api_response:
        print(f"{Fore.YELLOW}{word} : {Fore.GREEN}", api_response)
    else:
        print(f"{Fore.RED}[Debug] Error API ...")



def checklist(list):

    try:
        print(f"{Fore.RED}[+] {Fore.YELLOW}Password Check List :{Fore.GREEN}")
        with open(list, 'r', encoding='utf-8') as file:
            for line in file:
                word = line.strip()  # Remove any leading/trailing whitespace
                if word:  # Check if word is not empty
                    checkit2(word)
    except FileNotFoundError:
        print(f"{Fore.RED}File '{list}' not found.")
    except Exception as e:
        print(f"{Fore.RED}An error occurred : ", e)

