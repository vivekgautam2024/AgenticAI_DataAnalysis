import os
os.environ["STREAMLIT_SERVER_MAX_UPLOAD_SIZE"] = "2000"
os.environ["OPENAI_API_KEY"] = "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"
import streamlit as st

# Set Streamlit to wide mode
st.set_page_config(layout="wide", page_title="Main Dashboard", page_icon="📊")


data_visualisation_page = st.Page(
    "./Pages/python_visualisation_agent.py", title="Data Visualisation", icon="📈"
)

pg = st.navigation(
    {
        "Visualisation Agent": [data_visualisation_page]
    }
)

pg.run()
