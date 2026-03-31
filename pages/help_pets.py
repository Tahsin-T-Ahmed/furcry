import streamlit as st
from scraping import lmp_scraper

st.set_page_config(
    page_title = "FurCry: Help Pets",
    page_icon = ":material/pets:"
)

st.markdown("## :material/pets: Help Pets")
st.space()

if "poster_url" not in st.session_state:
    st.session_state["poster_url"] = ""


def handle_posting_url_entered():
    if "poster_url" not in st.session_state:
        return
    url = st.session_state["poster_url"].strip()

    st.session_state["url_warning"] = ""
    if not url:
        st.session_state["url_warning"] = 'Enter a URL first! Then, click "Scan URL"'
        return
    
    if (
        "lostmydoggie.com" in url
        or
        "lostmykitty.com" in url
    ):
        st.session_state["scraping_results"] = lmp_scraper.scrape(url)
        return
    
    st.session_state["url_warning"] = f"Invalid URL: {url}"
    return

    
    
posting_url = st.text_input(
    label = "Webpage URL",
    placeholder = "https://www.lostmydoggie.com/details.cfm?petid=473750",
    key = "poster_url",
    on_change = handle_posting_url_entered
)

if (
    "url_warning" in st.session_state
    and
    st.session_state["url_warning"]
):
    st.error(st.session_state["url_warning"])
    st.session_state["url_warning"] = ""

urlscanbtn = st.button(
    label = "Scan URL",
    type = "primary",
    on_click = handle_posting_url_entered
)

def display_scraped_info(scraping_results):
    lmp_scraper.format(scraping_results)


if "scraping_results" in st.session_state:
    display_scraped_info(st.session_state["scraping_results"])