import streamlit as st

@st.cache_data
def format(results:dict):
    lcol, rcol = st.columns([3, 2])
    with rcol:
        st.image(results["IMG_URL"])

    with lcol:
        for key in results:

            val = results[key]

            match(key):
                case "IMG_URL" | "PET ID" | "PET TYPE":
                    continue
                case "PET NAME":
                    val = f'"{val}"'
                case "TITLE":
                    st.subheader(val)
                    continue
                case _:
                    pass
            st.write(f"{key}: {val}")