from bs4 import BeautifulSoup
import requests

def scrape(url:str) -> dict:
    url = url.strip()

    response = requests.get(url)

    if 200 != response.status_code:
        return f"Invalid response from server. Status code: {response.status_code}"
    
    dom = BeautifulSoup(response.text, "html.parser")

    posting_info = {}

    header_words = dom.find("h1").text.split(' ')
    posting_info["TITLE"] = ' '.join(header_words[:2])
    
    lost_or_found = header_words[0]
    date = dom.find(string=f"{lost_or_found} Date").next_element.text
    date_terms = date.split('/')
    date = f"{date_terms[2]}-{int(date_terms[0]):02d}-{int(date_terms[1]):02d}"
    posting_info[f"DATE {lost_or_found.upper()}"] = date

    
    
    return posting_info

if "__main__" == __name__:
    url = input("Enter a URL:")
    print(scrape(url.strip()))