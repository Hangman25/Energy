import streamlit as st
from prediction import show_prediction
from about import show_about
from metar import show_metar
from taf import show_taf
from cloud import show_cloud
from solar import visualize_csv


st.set_page_config(layout="wide", page_title="🌤️ Energy Prediction Dashboard")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["About", "Prediction","METAR","TAF","Cloud Forecast","Solar Parameters"])

if page == "About":
    show_about()
elif page == "Prediction":
    show_prediction()
elif page == "METAR":
    show_metar()
elif page == "Cloud Forecast":
    show_cloud()
elif page == "TAF":
    show_taf()
elif page == "Solar Parameters":
    file_name = "csv/solar_2025.csv"  
    visualize_csv(file_name)  