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
    url = st.session_state["poster_url"].strip()

    st.session_state["url_warning"] = ""
    if not url:
        st.session_state["url_warning"] = 'Enter a URL first! Then, click "Scan URL"'
        return

    st.session_state["scraping_results"] = lmp_scraper.scrape(url)
    
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

if "scraping_results" in st.session_state:
    st.write(st.session_state["scraping_results"])