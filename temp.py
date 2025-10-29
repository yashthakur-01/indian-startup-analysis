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
    temp2 = df.loc[idx][['startup','amount']]
    st.dataframe(temp2)
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    
    # biggest investments till now
    coll1,coll2 = st.columns([1,1])
    with coll1:
        st.subheader('Biggest investments till now')
        temp3 = df[df['investor'].str.contains(option,na=False)].groupby('startup',as_index=False)\
        ['amount'].sum().sort_values('amount',ascending=False).reset_index(drop=True).head()
        fig,ax=plt.subplots()
        ax.bar(temp3['startup'],temp3['amount'])
        st.pyplot(fig)
        st.markdown("<br><br>", unsafe_allow_html=True)

    
    # amount of money invested in each vertical
    with coll2:
        st.subheader('Money invested in each vertical')
        temp = df[df['investor'].str.contains(option)].groupby('vertical')['amount'].sum()
        fig,ax = plt.subplots()
        ax.pie(temp,labels=temp.index)
        st.pyplot(fig)
        
        
    col1,col2 = st.columns([1,1])
    with col1:
        st.subheader('Money invested in each stage')
        temp = df[df['investor'].str.contains(option)].groupby('round')['amount'].sum()
        fig,ax = plt.subplots()
        ax.pie(temp,labels=temp.index)
        st.pyplot(fig)
        
    with col2:
        st.subheader('Money invested in each city')
        temp = df[df['investor'].str.contains(option)].groupby('city')['amount'].sum()
        fig,ax = plt.subplots()
        ax.pie(temp,labels=temp.index)        
        st.pyplot(fig)
        
        
    st.subheader("Year on year investment amount")
    print(df.info())
    temp = df[df['investor'].str.contains(option)].groupby(df['date'].dt.year)['amount'].sum()
    fig,ax = plt.subplots()
    ax.plot(temp.index,temp)
    plt.xticks(temp.index,labels=temp.index.astype(str))
    st.pyplot(fig)
        
     
     
def generalAnalysis():  
    
    col1,col2,col3,col4 = st.columns(4)
    with col1:
        # total invested amount over the years
        total = round(df['amount'].sum(),3)
        st.metric('Total',str(total)+ 'Cr')
    
    with col2:
        # maximum amount infused in a startup
        temp = df.groupby('startup')['amount'].max().sort_values(ascending=False)
        max_funding = temp.head(1).values[0]
        st.metric('Max',str(max_funding)+"Cr")

    with col3:
        # average ticket size
        Avg_funding = round(df.groupby('startup')['amount'].sum().mean(),2)
        st.metric('Average',str(Avg_funding)+"Cr")

    with col4:
        # Total funded startups
        count = df['startup'].nunique()        
        st.metric('Count',count)
            
    st.subheader("MoM Chart")  
    option11 = st.selectbox('select one',['Total','Count'])
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    if option11 == 'Total':
        temppp = df.groupby(['year', 'month'])['amount'].sum().reset_index()
        temppp['x-axis'] = temppp['year'].astype(str)+"-"+temppp['month'].astype(str)
        st.write(temppp)
    elif option11 == 'Count':
        temppp = df.groupby(['year', 'month'])['amount'].count().reset_index()
        temppp['x-axis'] = temppp['year'].astype(str)+"-"+temppp['month'].astype(str)



    fig,ax = plt.subplots()
    ax.plot(temppp['x-axis'],temppp['amount'])
    #ax.set_xticklabels(temp['x-axis'], rotation=90, ha='right')  # rotate labels for readability
    st.pyplot(fig)

# Download latest version
path = 'C:/Users/yasht/OneDrive/Desktop/fast api/streamlit/startup_cleaned (1).csv'


df = pd.read_csv(path,  )


st.sidebar.title('Startup Funding Analysis')
option = st.sidebar.selectbox('Select One',['Overall Analysis','Startup','Investor'])
state = st.session_state
if option == 'Overall Analysis':
    if 'show_overall' not in state:
        state.show_overall = False
        
    btn0 = st.sidebar.button('Show overall analysis')
    
    st.title('Overall Anlysis')
    if(btn0):
        state.show_overall = True
    if state.show_overall:
        generalAnalysis()



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
            
            
            
