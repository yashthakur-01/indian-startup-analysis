import pandas as pd
import numpy as np
import streamlit as st

def investor_details(option):
    temp = df[df["investor"].str.contains(option,na=False)]
    return temp.sort_values('date',ascending=False)


# Download latest version
path = 'C:/Users/yasht/OneDrive/Desktop/fast api/streamlit/startup_cleaned.csv'


df = pd.read_csv(path)


st.sidebar.title('Startup Funding Analysis')
option = st.sidebar.selectbox('Select One',['Overall Analysis','Startup','Investor'])

if option == 'Overall Analysis':
    st.title('Overall Anlysis')
elif option == 'Startup':
    st.sidebar.selectbox(' company',(df['startup'].unique()).tolist())
    st.title('Startup Analysis')
    btn1 = st.sidebar.button('Find Startup Details')
elif option == 'Investor':
    option = st.sidebar.selectbox('select investor',(sorted(set(df['investor'].str.split(',').sum()))))
    st.title('Investor Anlysis')
    btn2 = st.sidebar.button('Find Investor Details')
    if(btn2):
        col1,col2,col3 = st.columns([1,2,1])
        with col2:
            st.header(option)
            st.markdown("<br><br>", unsafe_allow_html=True)
            st.dataframe(investor_details(option))
            
            
