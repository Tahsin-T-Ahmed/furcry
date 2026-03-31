from bs4 import BeautifulSoup
import requests

def scrape(url:str) -> dict:
    url = url.strip()

    response = requests.get(url)

    if 200 != response.status_code:
        return f"Invalid response from server. Status code: {response.status_code}"
    
    dom = BeautifulSoup(response.text, "html.parser")

    posting_info = {}
    
    posting_info["TITLE"] = ' '.join(dom.find("h1").text.split(' ')[:2])
    
    return posting_info

if "__main__" == __name__:
    url = input("Enter a URL:")
    print(scrape(url.strip()))