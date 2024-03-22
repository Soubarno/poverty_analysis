import streamlit as st

st.set_page_config(
    page_title = 'Poverty Analysis',
    page_icon = '🌟',
    layout = 'wide',
    initial_sidebar_state = 'auto'
)

from web_functions import load_data

from Tabs import home, data, predict, predict1, visualise

Tabs = {
    "Home": home,
    "Data Info": data,
    "Prediction - State": predict,
    "Prediction - Area": predict1,
    "Visualisation": visualise    
}

st.sidebar.title("Navigation")
st.sidebar.image("./images/home.png")

page = st.sidebar.radio("Pages", list(Tabs.keys()))

df, X, y = load_data()

if page in ["Prediction - State","Prediction - Area", "Visualisation"]:
    Tabs[page].app(df, X, y)
elif (page == "Data Info"):
    Tabs[page].app(df)
else:
    Tabs[page].app()
