import streamlit as st

homepage = st.Page(
    page = "./pages/home.py",
    title = "Homepage",
    icon = ":material/home:"
)

help_pets = st.Page(
    page = "./pages/help_pets.py",
    title = "Help Pets",
    icon = ":material/pets:"
)

dev = st.Page(
    page = "./pages/developer.py",
    title = "Developer",
    icon = ":material/person:"
)

nav = st.navigation(
    pages = [homepage, help_pets, dev],
    position = "top"
)

nav.run()