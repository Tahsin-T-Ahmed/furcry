import streamlit as st

st.set_page_config(
    page_title = "FurCry: Help Pets",
    page_icon = ":material/pets:"
)

st.header("Help Pets")
st.space()

posting_url = st.text_input(
    label = "Webpage URL",
    placeholder = "https://www.lostmydoggie.com/details.cfm?petid=473750",
    key = "poster_url"
)

def handle_urlscanbtn_click():
    url = st.session_state["poster_url"].strip()

    st.session_state["url_warning"] = ""
    if not url:
        st.session_state["url_warning"] = 'Enter a URL first! Then, click "Scan URL"'
        return

url_btn_col, warning_col = st.columns([1, 6])
with url_btn_col:
    urlscanbtn = st.button(
        label = "Scan URL",
        type = "primary",
        on_click = handle_urlscanbtn_click
    )

with warning_col:
    st.error(st.session_state["url_warning"])