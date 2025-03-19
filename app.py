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
import threading

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

def run_continuously(interval=1):
    """Continuously run, while executing pending jobs at each
    elapsed time interval.
    @return cease_continuous_run: threading. Event which can
    be set to cease continuous run. Please note that it is
    *intended behavior that run_continuously() does not run
    missed jobs*. For example, if you've registered a job that
    should run every minute and you set a continuous run
    interval of one hour then your job won't be run 60 times
    at each interval but only once.
    """
    cease_continuous_run = threading.Event()

    class ScheduleThread(threading.Thread):
        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                schedule.run_pending()
                time.sleep(interval)

    continuous_thread = ScheduleThread()
    continuous_thread.start()
    return cease_continuous_run

# Schedule the email job
# schedule.every(1).minutes.do(send_email_job)

# Start the background thread
# stop_run_continuously = run_continuously()

# Do some other things...
# time.sleep(10)

# Stop the background thread
# stop_run_continuously.set()
