import requests # type: ignore

def directory_bruteforce(url: str, wordlist: list) -> list:
    found_paths = []
    for word in wordlist:
        target_url = f"{url}/{word}"
        response = requests.get(target_url)
        if response.status_code == 200:
            found_paths.append(target_url)
    return found_paths
