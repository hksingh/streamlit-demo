import calendar # core python module
import streamlit as st #pip install streamlit
import plotly.graph_objects as go # pip install plotly
from datetime import datetime # core python module
from streamlit_option_menu import option_menu # pip install streamlit-option-menu
from dbsetup import getKey

page_title = "Income and Expense Tracker12"
page_icon=":money_with_wings:"
layout = "wide"
currency= "USD"

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)

# --- Drop down values for selecting period
years = [datetime.today().year-1, datetime.today().year]
months = list(calendar.month_name[1:])

# --- HIDE STREAMLIT STYLE ---
hide_st_style = """
                <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    header {visibility: hidden;}
                </style>
                """

st.markdown(hide_st_style, unsafe_allow_html=True)

# --- NAVIGATION MENU ---
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu", #required
        options=["Home", "Projects", "Contact"]
    )

if selected == "Home":
    st.title(f"You have selected {selected}")
if selected == "Projects":
    st.title(f"You have selected {selected}")
if selected == "Contact":
    st.title(f"You have selected {selected}")

# --- INPUT & SAVE PERIODS ---
st.header(f'Data Entry in {currency}')
value = getKey()
st.subheader(f'Deta Key {value}')
# with st.form("entry_form", clear_on_submit=True):
#     col1, col2 = st.columns(2)
#     col1.selectbox("Select Month : ", months, key="month")
#     col2.selectbox("Select Year : ", years, key="year")
