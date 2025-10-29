import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(layout='wide',page_title ="Indian startup analysis")
                   
                   
                   
def investor_details(option):
    st.header(option)
    st.markdown("<br><br>", unsafe_allow_html=True)
    # load most recent investments.
    st.subheader('Most recent investments.')
    temp = df[df["investor"].str.contains(option,na=False)]
    st.dataframe(temp.sort_values('date',ascending=False).head()[['date','startup','vertical','city','round','amount']])
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    
    # biggest investment in each startup
    st.subheader('Biggest Investment in each Company')
    idx = df[df['investor'].str.contains(option, na=False)] \
    .groupby('startup')['amount'].idxmax()
    print (idx)
    temp2 = df.loc[idx][['startup','amount']]
    print(temp2)
    st.dataframe(temp2)
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    
    # biggest investments till now
    st.subheader('Biggest investments till now')
    temp3 = df[df['investor'].str.contains(option,na=False)].groupby('startup',as_index=False)\
    ['amount'].sum().sort_values('amount',ascending=False).reset_index(drop=True).head()
    fig,ax=plt.subplots()
    ax.bar(temp3['startup'],temp3['amount'])
    st.pyplot(fig)
    

# Download latest version
path = 'C:/Users/yasht/OneDrive/Desktop/fast api/streamlit/startup_cleaned (1).csv'


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
        col1,col2,col3 = st.columns([1,6,1])
        with col2:
            investor_details(option)
            
            
            
