import streamlit as st
import time
# ***********text utilities*****************
st.title('startup Dashboard')
st.header('I am learning streamlit')
st.subheader('yash thakur')
st.write('this is a normal text')
st.markdown('''
            ### movie names
            - race three
            - jawaan
            - bawaal
            ''')
st.code('''
        int c = 0;
        cout<< 'square' << " "<<c*c;
        ''')
# for mathematical symbols
st.latex('x^2 + y^2 = c^2')

import streamlit as st
# ***********display elements*****************

import pandas as pd
df = pd.DataFrame({
    'name':['yash','shivans','nitish'],
    'marks':[56,67,78],
    'package':[10,12,40]
})
st.dataframe(df)

# st.metric('metric name','metricvalue','increase or decrease ')
st.metric('Revenue','Rs 3L','-3%')

st.json({
    'name':['yash','shivans','nitish'],
    'marks':[56,67,78],
    'package':[10,12,40]
})

# ***********displaying media*****************
st.image('C:/Users/yasht/OneDrive/Desktop/fast api/streamlit/WhatsApp Image 2025-06-14 at 10.56.38_1082ec70.jpg')
st.video('C:/Users/yasht/OneDrive/Desktop/fast api/streamlit/WhatsApp Video 2025-06-15 at 22.53.40_82cb2712.mp4')


# ***********showing layouts*****************
st.sidebar.title ('sidebar ka title')

col1,col2,col3 = st.columns(3)
with col1:
    st.title('column 1')
    
with col2:
    st.title('column 2')
    
with col3:
    st.title('column 3')
# ***********showing status*****************    
st.error('login failed')
st.success('login success')
st.warning('warning')
st.info('information')

# progress bar
bar = st.progress(0)

for i in range(0,101):
#    time.sleep(0.1)
    bar.progress(i)
    
# ***********taking inputs*****************    
email = st.text_input('enter email address')
number = st.number_input('enter age')
date = st.date_input('enter date of birth')

# buttons
user = st.text_input('enter username')
password = st.text_input('enter password')
# dropdowns

gender = st.selectbox('select gender',['male','female','others'])

btn = st.button('login')
if btn:
    if user == 'yash' and password == '1234':
        st.success('login successful. welcome!')
        st.write(user)
        st.write(gender)
        st.balloons()
    else:
        st.error('unidentified user!!!')


# file uploader
files = st.file_uploader('upload a file(max 10mb)')    

if files is not None:
    df = pd.read_csv(files)
    st.dataframe(df.describe())