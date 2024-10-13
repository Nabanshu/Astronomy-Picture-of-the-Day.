import streamlit as st 
import requests

st.set_page_config(page_title="Astronomy Picture of the Day.",layout="wide",page_icon=":material/rocket_launch:")

r = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={api}")
content = r.json()

col1, col2 = st.columns([0.6,0.5],vertical_alignment="center")
with col1:
    st.title(content["title"])
    if content["media_type"] == "video":
        st.video(content["url"])
    else:
        try:
            st.image(content["url"],caption=[(content["date"])+"    "+content["copyright"]])
        except:
            st.image(content["url"])
with col2:
    st.info(content["explanation"])





