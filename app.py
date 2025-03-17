import streamlit as st
import schedule
import time
from scripts.prediction import show_prediction
from scripts.about import show_about
from scripts.metar import show_metar
from scripts.taf import show_taf
from scripts.cloud import show_cloud
from scripts.solar import visualize_csv
from scripts.location import show_location_predictions
from scripts.send_email_job import send_email_job
from threading import Thread

st.set_page_config(layout="wide", page_title="🌤️ Energy Prediction Dashboard")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["About", "Prediction", "METAR", "TAF", "Cloud Forecast", "Solar Parameters", "Location"])

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
    visualize_csv("csv/solar_2025.csv")
elif page == "Location":
    show_location_predictions()

schedule.every().day.at("14:25").do(send_email_job)
  #  schedule.every().day.at("10:58","America/Halifax").do(send_email_job)
   # schedule.every().day.at("16:01").do(send_email_job)
    
while True:
    schedule.run_pending()
    time.sleep(1)

#if 'scheduler_thread' not in st.session_state:
 #   st.session_state.scheduler_thread = Thread(target=run_scheduler,daemon=True)
  #  st.session_state.scheduler_thread.start()
        

#schedule.every().minutes.do(send_email_job)
