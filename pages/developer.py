from PIL import Image
import streamlit as st

st.set_page_config(
    page_title = "FurCry: Developer",
    page_icon = ":material/pets:"
)

st.markdown("## :material/person: About the Developer")
github_url = "https://github.com/Tahsin-T-Ahmed"
repo_url = "https://github.com/Tahsin-T-Ahmed/furcry"
linkedin_url = "https://www.linkedin.com/in/tahsin-t-ahmed/"
email_address = "tahsin.t.ahmed@gmail.com"

dev_pic = Image.open("./static/IMG-20220625-WA0000.jpg")
dev_pic = dev_pic.crop((0, 100, dev_pic.width, dev_pic.height-150))

st.markdown(f"### Hi there! I'm [Tahsin]({github_url}).")

lcol1, rcol1 = st.columns([2, 3])

with lcol1:    
    st.write(dev_pic)
    st.caption("Feeding my baby Hercules.")

with rcol1:
    st.markdown("#### Why did I build FurCry?")
    st.write("""
        As someone involved in the online communities of Lost & Found pets, 
        I often found myself manually typing out alert messages 
        to spread awareness about missing pets on various online platforms 
        (such as Ring (Neighbors), Nextdoor, Facebook, etc),
        especially upon receiving alerts from LostMyKitty and LostMyDoggie.
    """)
    st.write("""
        FurCry makes the process quick and easy, so we can alert our friends,
        neighborhoods, communities, groups, and more -- as efficiently as possible!
    """)

st.divider()

lcol2, rcol2 = st.columns(2)
with lcol2:
    st.markdown("#### This project is open-source.")
    st.markdown(f"##### Check out the [Github Repository :material/folder_code:]({repo_url})")
    st.write(repo_url)
    st.write("Your feedback/suggestions/contributions are appreciated.")
    st.write("Let's help reunite as many pets as possible!")

with rcol2:
    st.markdown("#### Contact Me")
    st.markdown(f"##### Let's connect on [LinkedIn :material/account_box:]({linkedin_url})")
    st.markdown(f"##### Or you can [Email Me :material/mail:](mailto:{email_address})")
    st.markdown(f"##### Also, follow my [GitHub :material/code:]({github_url})")