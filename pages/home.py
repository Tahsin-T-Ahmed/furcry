import streamlit as st

st.set_page_config(
    page_title = "FurCry: Help Reunite Lost Pets",
    page_icon = ":material/pets:"
)

st.markdown("# :material/pets: FurCry: Missing Pets Need You!")

st.space()

st.header("What is FurCry?")
st.caption("""
    FurCry takes information from alerts of Lost/Found pets,
    and processes it into a sharable format for spreading awareness 
    on various platforms (such as social media, messaging, email, etc) 
    as quickly and efficiently as possible.
""")

st.markdown("Ready to start helping? Go to the :red[Help Pets] tab or click below:")
st.page_link(
    page = "./pages/help_pets.py",
    label = "Help Pets",
    icon = ":material/pets:"
)
