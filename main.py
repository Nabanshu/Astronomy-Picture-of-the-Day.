import streamlit as st 
import requests


st.set_page_config(page_title="Astronomy Picture of the Day.",layout="wide",page_icon=":material/rocket_launch:")

r = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={st.secrets["API_KEY"]}&concept_tags=True&thumbs=True&hd=True")
content = r.json()


st.title("Astronomy Picture of the Day",help="Discover the cosmos with NASA's most popular website! The APOD API provides daily stunning astronomy images, metadata, and optional concept tags for enhanced discoverability.")
col1, col2 = st.columns([0.6,0.5],vertical_alignment="center")
with col1:
    st.title(content["title"])
    if content["media_type"] == "video" or "other":
        try:
            st.video(content["url"])
        except KeyError:
            st.warning("Image/Video not found, wait for the next APOD",icon=":material/error:")
    else:
        try:
            st.image(content["hdurl"],caption=((content["date"])+ "" +content["copyright"]))
        except KeyError:
            if "copyright" in content:
                st.image(content["url"],caption=((content["date"])+ "" +content["copyright"]))
            else:
                st.image(content["url"],caption=(content["date"]))
                    
with col2:
    st.info(content["explanation"])




