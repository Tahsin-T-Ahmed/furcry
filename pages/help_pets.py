import streamlit as st

st.set_page_config(
    page_title = "FurCry: Help Pets",
    page_icon = ":material/pets:"
)

st.markdown("## :material/pets: Help Pets")
st.space()


def handle_posting_url_entered():
    url = st.session_state["poster_url"].strip()

    st.session_state["url_warning"] = ""
    if not url:
        st.session_state["url_warning"] = 'Enter a URL first! Then, click "Scan URL"'
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