import streamlit as st

st.header("Help Pets")
st.space()
posting_url = st.text_input(
    label = "Webpage URL (e.g, https://www.lostmydoggie.com/details.cfm?petid=473750)",
    placeholder = "Paste URL here"
)

def handle_urlscanbtn_click():
    pass

urlscanbtn = st.button(
    label = "Scan URL",
    on_click = handle_urlscanbtn_click
)