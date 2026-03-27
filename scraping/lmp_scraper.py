from bs4 import BeautifulSoup
import requests

def scrape(url:str) -> dict:
    response = requests.get(url)
    if 200 != response.status_code:
        return f"Invalid response from server. Status code: {response.status_code}"
    
    dom = BeautifulSoup(response.text, "html.parser")

    details_table = dom.find("table")

    rows = details_table.find_all("tr")

    posting_info = {}

    for row in rows:
        # continue
        columns = row.find_all("td")

        key = columns[0].text
        val = None

        if 2 == len(columns):
            val = columns[1].text

            posting_info[key] = val

    return posting_info

if "__main__" == __name__:
    url = input("Enter a URL:")
    print(scrape(url.strip()))