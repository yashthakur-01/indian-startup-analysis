import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout='wide',page_title ="Indian startup analysis")




def startup_details(option):
    temp = df[df['startup_name']==option]
    
    
    vertical = ','.join(temp['vertical'].unique()[:5])
    location = temp['city'].head(1).values[0]
    st.subheader(f"Industry: {vertical}")
    st.subheader(f"Location: {location}")
    
    col1,col2,col3 = st.columns(3)
    highest = temp['amount'].max()
    average = temp[temp['amount']!=0]['amount'].mean()
    if np.isnan(average):
        average = 0 
    count = temp.shape[0]
    col1.metric("Highest Investment",f"₹{highest:.2f} Cr")
    col2.metric("Average Investment",f"₹{average:.2f} Cr")
    col3.metric("Total Investment",count)
    st.write('---')
    
    
    col1,col2 = st.columns([1,1])
    if 'btn1' not in st.session_state:
        st.session_state.btn1 = True
    if 'btn2' not in st.session_state:
        st.session_state.btn2 = False
    
    
    if col1.button("Recent Investment"):
        st.session_state.btn1 = True
        st.session_state.btn2 = False  
        st.session_state.btn3 = False  
        st.session_state.btn4 = False  
    if col2.button("Biggest Investment"):
        st.session_state.btn2 = True
        st.session_state.btn1 = False
        st.session_state.btn3 = False
        st.session_state.btn4 = False
    
    
    st.write("---")

    if st.session_state.btn1:
         # Recent investments
        st.subheader("1. Recent investments received")
        x = temp.sort_values('date',ascending=False)[['date','investor_name','amount']]
        st.table(x.reset_index(drop=True))
        st.markdown("<br><h4>Line Chart<h4/>",unsafe_allow_html=True)
        st.line_chart(data=x,x='date',y='amount',x_label='Date',y_label='Amount(Cr)')
        st.write("---")
    
    if st.session_state.btn2:
        # Biggest Investments till now
        x = temp.sort_values('amount',ascending=False) 
        st.subheader("2. Biggest investments received")
        st.table(x[['date','investor_name','amount']].reset_index(drop=True))
        st.markdown("<br><h4>Line Chart<h4/>",unsafe_allow_html=True)
        st.line_chart(data=x,x='date',y='amount',x_label='Date',y_label='Amount(Cr)')
        st.write("---")
    
    col1,col2 = st.columns(2)
    
    col1.subheader("Investment by Stage")    
    col1.text('Percent funding received each stage.')
    stage = temp.groupby('type')['amount'].sum()
    fig1,ax1 = plt.subplots()
    ax1.pie(stage,labels = stage.index,autopct='%.1f%%')
    col1.pyplot(fig1)
    
    col2.subheader("Investment by year")    
    col2.text('Total funding received each year.')
    temp['year'] = temp['date'].dt.year
    stage = temp.groupby('year')['amount'].sum()
    fig2,ax2= plt.subplots()
    ax2.bar(stage.index.astype(str),stage.values)
    ax2.set_xlabel('Year')
    ax2.set_ylabel('Amount (Cr)')
    plt.xticks(rotation=0)
    col2.pyplot(fig2)
        
    
    st.markdown('<br>',unsafe_allow_html=True)
    st.error('''Note 
                           
             - 0 Cr amount indicates the investment amount is not disclosed.
             - All the metrics like average and total are calculated excluding the "not disclosed" investments.''')
 
 
 
    

def overall_analysis():
    col1,col2,col3,col4 = st.columns(4)
    with col1:
        # total invested amount over the years
        total = round(df['amount'].sum(),3)
        st.metric('Total',str(total)+ 'Cr')
    
    with col2:
        # maximum amount infused in a startup
        temp = df.groupby('startup_name')['amount'].max().sort_values(ascending=False)
        max_funding = temp.head(1).values[0]
        st.metric('Max',str(max_funding)+"Cr")

    with col3:
        # average ticket size
        Avg_funding = round(df.groupby('startup_name')['amount'].sum().mean(),2)
        st.metric('Average',str(Avg_funding)+"Cr")

    with col4:
        # Total funded startups
        count = df['startup_name'].nunique()        
        st.metric('Count',count)
    st.write("---")       
    st.subheader("MoM Chart")  
    st.text("Month on Month investment in the startups.")
    option11 = st.selectbox('select one',['Total','Count'])
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    if option11 == 'Total':
        st.text('Month on Month Funding inflow (amount) in the startups.')
        temppp = df.groupby(['year', 'month'])['amount'].sum().reset_index()
        temppp['x-axis'] = temppp['year'].astype(str)+"-"+temppp['month'].astype(str)
    elif option11 == 'Count':
        st.text('Month on Month Count of startups that received the Fundings.')
        temppp = df.groupby(['year', 'month'])['amount'].count().reset_index()
        temppp['x-axis'] = temppp['year'].astype(str)+"-"+temppp['month'].astype(str)
    
    st.line_chart(data=temppp, x='x-axis', y='amount',x_label='Year-Month', y_label='Amount/Count')
    
    # top startups
    st.write("---")
    st.subheader("Top Startups")
    st.text('Top startups on the basis of Funding Amount received Over the Years.')
    option = st.selectbox("",['Year-Wise','Overall'],index=1,key='top_startup')
    col1,col2,col3 = st.columns([1,7,1])
    if option == 'Year-Wise':
        temp = df.copy()
        temp['year'] = temp['date'].dt.year
        x = temp.groupby(['year','startup_name'])['amount'].sum().reset_index().sort_values(['year','amount'],ascending=[True,False]).groupby('year').head(3)
        
        fig,ax = plt.subplots(figsize=(10, 6))
        sns.barplot(data = x, x='year',y='amount',hue='startup_name',ax=ax)
        
        ax.set_title("Top 3 Startups Each Year (by Funding Amount)")
        ax.set_xlabel("Year")
        ax.set_ylabel("Total Funding Amount")
        ax.legend(title="Startup", bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        col2.pyplot(fig)
        
    if option == 'Overall':
        temp = df.copy()
        x = temp.groupby('startup_name')['amount'].sum().sort_values(ascending=False).reset_index().head(10)
        fig,ax = plt.subplots(figsize=(10,6))
        sns.barplot(data=x,x='startup_name',y='amount',ax=ax)
        
        ax.set_title("Top 10 Overall startups (by Funding Amount)")
        ax.set_xlabel("Startup Name")
        ax.set_ylabel("Total Funding Amount")
        plt.tight_layout()
        col2.pyplot(fig)
        
        
    # top investors
    
    st.write("---")
    st.subheader("Top Investors")
    st.text('Top Investors on the basis of Funding Amount given Over the Years.')
    option1 = st.selectbox("",['Year-Wise','Overall'],index=1,key='top_investor')
    if option1 == 'Year-Wise':
        temp = df.copy()
        temp['year'] = temp['date'].dt.year
        x = temp.groupby(['year','investor_name'])['amount'].sum().reset_index().sort_values(['year','amount'],ascending=[True,False]).groupby('year').head(3)
        
        fig,ax = plt.subplots(figsize=(10, 6))
        sns.barplot(data = x, x='year',y='amount',hue='investor_name',ax=ax)
        
        ax.set_title("Top 3 Investors Each Year (by Funding Amount)")
        ax.set_xlabel("Year")
        ax.set_ylabel("Total Funding Amount")
        ax.legend(title="Startup", bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        st.pyplot(fig)
        
    if option1 == 'Overall':
        col1,col2 = st.columns([1.9,1.1])
        temp = df.copy()
        x = temp.groupby('investor_name')['amount'].sum().sort_values(ascending=False).reset_index().head(10)
        count = temp[temp['investor_name'].isin(x['investor_name'])].groupby('investor_name')['amount'].count().reset_index()
        count.rename(columns={'investor_name':'Investors','amount':'No. of investments'},inplace=True)
        fig,ax = plt.subplots(figsize=(10,6))
        sns.barplot(data=x,x='investor_name',y='amount',ax=ax)
        
        ax.set_title("Top 10 Overall Investors (by Funding Amount)")
        ax.set_xlabel("Startup Name")
        ax.set_ylabel("Total Funding Amount")
        ax.tick_params(axis='x',rotation=45)
        plt.tight_layout()
        col1.pyplot(fig)
        col2.dataframe(count[['Investors','No. of investments']])
        
    
    
    #sector Analysis
    
    st.write('---')
    st.subheader('Sector Analysis')
    sec = df['vertical'].nunique()
    st.metric('Total sectors',sec)
    col1,col2 = st.columns(2)
    
    col1.text('Total investment count in top 10 sectors.')
    fig1,ax1 = plt.subplots(figsize=(14,7))
    x = df.groupby('vertical')['amount'].count().sort_values(ascending=False).head(10)
    ax1.pie(x,labels=x.index,autopct='%.2f%%')
    col1.pyplot(fig1)
    
    col2.text('Total investment amount in top 10 sectors.')
    fig2,ax2 = plt.subplots(figsize=(14,9.5))
    x = df.groupby('vertical')['amount'].sum().sort_values(ascending=False).head(10)
    ax2.bar(x.index,x.values)
    ax2.tick_params(axis='x', rotation=50)
    col2.pyplot(fig2)


    # Funding type
    
    st.write('---')
    st.subheader('Stage Analysis')
    col1,col2 = st.columns(2)
    
    col1.text('Total investment count in different stages.')
    fig1,ax1 = plt.subplots(figsize=(14,4))
    x = df.groupby('type')['amount'].count().sort_values(ascending=False).head(10)
    ax1.pie(x,labels=x.index,autopct='%.2f%%')
    col1.pyplot(fig1)
    
    col2.text('Total investment amount in different stages.')
    fig2,ax2 = plt.subplots(figsize=(14,9.5))
    x = df.groupby('type')['amount'].sum().sort_values(ascending=False).head(10)
    ax2.bar(x.index,x.values)
    ax2.tick_params(axis='x', rotation=50)
    col2.pyplot(fig2)
    
    # City wise analysis
    st.write('---')
    st.subheader('City-wise Analysis')
    col1,col2 = st.columns(2)
    
    col1.text('Total startup count in different cities.')
    fig1,ax1 = plt.subplots(figsize=(14,4))
    x = df.groupby('city')['amount'].count().sort_values(ascending=False).head(10)
    ax1.pie(x,labels=x.index,autopct='%.2f%%')
    col1.pyplot(fig1)
    
    col2.text('Total investment amount in different cities.')
    fig2,ax2 = plt.subplots(figsize=(14,9.5))
    x = df.groupby('city')['amount'].sum().sort_values(ascending=False).head(10)
    ax2.bar(x.index,x.values)
    ax2.tick_params(axis='x', rotation=50)
    col2.pyplot(fig2)
    
    
    
    
    

def investor_details(option):
    
    temp = df[df['investor_name']==option]
    
    
    col1,col2,col3 = st.columns(3)
    highest = temp['amount'].max()
    average = temp[temp['amount']!=0]['amount'].mean()
    if np.isnan(average):
        average = 0 
    count = temp.shape[0]
    col1.metric("Highest Investment",f"₹{highest:.2f} Cr")
    col2.metric("Average Investment",f"₹{average:.2f} Cr")
    col3.metric("Total Investment",count)
    st.write('---')
    
    st.markdown("<h3>General Investment Overview</h3><br>",unsafe_allow_html=True)
    
    col1,col2,col3,col4 = st.columns([1,1,1,1])
    if 'btn1' not in st.session_state:
        st.session_state.btn1 = True
    if 'btn2' not in st.session_state:
        st.session_state.btn2 = False
    if 'btn3' not in st.session_state:
        st.session_state.btn3 = False
    if 'btn4' not in st.session_state:
        st.session_state.btn4 = False
    
    if col1.button("Recent Investment"):
        st.session_state.btn1 = True
        st.session_state.btn2 = False  
        st.session_state.btn3 = False  
        st.session_state.btn4 = False  
    if col2.button("Biggest Investment"):
        st.session_state.btn2 = True
        st.session_state.btn1 = False
        st.session_state.btn3 = False
        st.session_state.btn4 = False
    if col3.button("Total Investment (each startup)"):
        st.session_state.btn3 = True
        st.session_state.btn1 = False
        st.session_state.btn2 = False
        st.session_state.btn4 = False
    if col4.button("Average Investment (each vertical)"):
        st.session_state.btn4 = True
        st.session_state.btn1 = False
        st.session_state.btn3 = False
        st.session_state.btn2 = False
    
    st.write("---")

    if st.session_state.btn1:
         # Recent investments
        st.subheader("1. Recent investments")
        x = temp.sort_values('date',ascending=False).head(7)[['date','startup_name','amount']]
        st.table(x.reset_index(drop=True))
        st.markdown("<br><h4>Line Chart<h4/>",unsafe_allow_html=True)
        st.line_chart(data=x,x='date',y='amount',x_label='Date',y_label='Amount(Cr)')
        st.write("---")
    
    if st.session_state.btn2:
        # Biggest Investments till now
        x = temp.sort_values('amount',ascending=False).head() 
        st.subheader("2. Biggest investments")
        st.table(x[['date','startup_name','amount']].reset_index(drop=True))
        st.markdown("<br><h4>Line Chart<h4/>",unsafe_allow_html=True)
        st.line_chart(data=x,x='date',y='amount',x_label='Date',y_label='Amount(Cr)')
        st.write("---")
    
    if st.session_state.btn3:
        # Total investments each startup
        st.subheader("3. Total investments")
        x = temp.groupby('startup_name')['amount'].sum()
        st.table(x)
        st.markdown("<br><h4>Line Chart<h4/>",unsafe_allow_html=True)
        st.line_chart(x)

    if st.session_state.btn4:
        # Average investments each vertical
        st.subheader("4. Average investments")
        x = temp.groupby('vertical')['amount'].mean().head(10)
        st.table(x)
        st.markdown("<br><h4>Line Chart<h4/>",unsafe_allow_html=True)
        st.line_chart(x)
        
        
    # piechart for vertical count and city count and funding round count
    col1,col2,col3 = st.columns(3)
    
    col1.subheader("Investment by Sector")
    col1.text('Which Sector/Vertical investor prefer.')
    vert = temp['vertical'].value_counts()
    fig,ax = plt.subplots()
    ax.pie(vert,labels = vert.index,autopct='%.1f%%')
    col1.pyplot(fig)
    
    col2.subheader("Investment by Stage")
    col2.text('Which startup stages the investor prefers.')
    stage = temp['type'].value_counts()
    fig1,ax1 = plt.subplots()
    ax1.pie(stage,labels = stage.index,autopct='%.1f%%')
    col2.pyplot(fig1)
    
    
    col3.subheader("Investment by city")
    col3.text('Which Geographic Location investor prefer.')
    vert = temp['city'].value_counts()
    fig,ax = plt.subplots()
    ax.pie(vert,labels = vert.index,autopct='%.1f%%')
    col3.pyplot(fig)
    st.write('---')
    
    st.markdown('<br>',unsafe_allow_html=True)

    #year on year investment trend.
    temp['year'] = temp['date'].dt.year
    yoy = temp.groupby('year')['amount'].sum()     
    st.subheader('Year on Year Investment Trend.')
    st.line_chart(yoy)

    st.markdown('<br>',unsafe_allow_html=True)
    st.error('''Note 
                           
             - 0 Cr amount indicates the investment amount is not disclosed.
             - All the metrics like average and total are calculated excluding the "not disclosed" investments.''')

    


                   
                   
df = pd.read_csv("startup_cleaned.csv",parse_dates=['date'])

st.markdown("<center><div><h1>Indian Startup Analysis</h1></div></center>", unsafe_allow_html=True)

sb = st.sidebar
sb.subheader("Choose an option")
option = sb.selectbox("",["Overall analysis",'Investor','Start-up'],index=0)


if option == "Overall analysis":
    st.title("Overall Analysis")
    overall_analysis()
    st.write("---")

if option == "Investor":
    investor = df['investor_name'].sort_values(ascending=True).unique()
    option = sb.selectbox("Choose an Investor",list(investor))
    st.write("---")
    st.title(f"Investor Analysis: {option}")
    
    st.markdown('<br>',unsafe_allow_html=True)    
    if 'investor_btn' not in st.session_state:
        st.session_state.investor_btn = False
    
    if sb.button('Find investor details'):
        st.session_state.investor_btn = True
        st.session_state.startup_btn = False
    if st.session_state.investor_btn:        
        investor_details(option)
  
    
if option == "Start-up":
    startup = df['startup_name'].sort_values(ascending=True).unique()
    option = sb.selectbox("Choose an Investor",list(startup))
    st.write("---")
    st.title(f"Startup Analysis - {option}")
    st.markdown('<br>',unsafe_allow_html=True)    
    if 'startup_btn' not in st.session_state:
        st.session_state.startup_btn = False
    
    if sb.button('Find investor details'):
        st.session_state.startup_btn = True
        st.session_state.investor_btn = False
    if st.session_state.startup_btn:        
        startup_details(option)
    
    
    
