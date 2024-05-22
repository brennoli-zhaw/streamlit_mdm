import streamlit as st
import folium
from streamlit_folium import st_folium
import requests

m = folium.Map(location=[39.8283, -98.5795], zoom_start=5)

# If you want to dynamically add or remove items from the map,
# add them to a FeatureGroup and pass it to st_folium
fg = folium.FeatureGroup(name="markers")

agree = st.checkbox("Lade Karte mit der Position der ISS")
r = requests.get('http://api.open-notify.org/iss-now.json').json()
if agree:
    r = requests.get('http://api.open-notify.org/iss-now.json').json()
    #st.write(r)
    
    lng = r["iss_position"]["longitude"]
    lat = r["iss_position"]["latitude"]
    marker = [lng,lat]
    fg.add_child(
        folium.Marker(
            location=marker,
            icon=folium.Icon(color="green")
        )
    )
    
    out = st_folium(
        m,
        feature_group_to_add=fg,
        center=marker,
        width=600,
        height=500,
    )
    
    
