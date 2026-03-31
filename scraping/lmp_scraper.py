from bs4 import BeautifulSoup
import requests

def scrape(url:str) -> dict:
    url = url.strip()
    response = requests.get(url)
    if 200 != response.status_code:
        return f"Invalid response from server. Status code: {response.status_code}"
    
    dom = BeautifulSoup(response.text, "html.parser")    

    posting_info = {}

    section_heading = dom.find("div", class_="section-heading").text.strip().split(' ')

    posting_info["TITLE"] = f"{' '.join(section_heading[:2])} in {' '.join(section_heading[2:])}"

    details_table = dom.find("table")

    rows = details_table.find_all("tr")

    for row in rows:
        td_list = row.find_all("td")

        key = None
        val = None

        if 2 == len(td_list):
            key = td_list[0].text[:-1].upper()
        elif 1 == len(td_list):
            key = td_list[0].find("h5").text[:-1].upper()
        else:
            return "Error! Invalid webpage format."

        if "PET " in key:
            key = key.split(' ')[1]

        match(key):
            case "NAME" | "TYPE" | "BREED" | "COLOR" | "GENDER" | "DATE LOST" | "DATE FOUND":
                val = td_list[1].text.strip()
            case "DESCRIPTION" | "AREA LAST SEEN" | "AREA FOUND" | "CROSS STREETS":
                val = td_list[0].find("p").text.strip()
            case _:
                continue

        posting_info[key] = val

        img_url_rel = dom.find("img", class_="center-block")["src"]
        posting_info["IMG_URL"] = f"{url[:28]}/pet_images/{img_url_rel.split('/')[-1]}"

        posting_info["NAME"] = posting_info["NAME"].split('(')[0]
        posting_info["ID"] = url.split("petid=")[1]

    posting_info["URL"] = url
    return posting_info

if "__main__" == __name__:
    url = input("Enter a URL:")
    print(scrape(url.strip()))