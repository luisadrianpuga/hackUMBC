import streamlit as st
import pandas as pd
import numpy as np
import requests


st.title("Capital One Hack")#########
###########



url = 'http://api.nessieisreal.com/customers?key=da4f6777887367bc27414d3d13157abe'
IMGurl = 'https://media.discordapp.net/attachments/903431149412548672/904082702150565908/hackUMBC_logo.png'

visa_url = "https://sandbox.api.visa.com/globalatmlocator/v1/localatms/atmsinquiry"

#page title
st.sidebar.image(IMGurl)
st.sidebar.title("2021 UMBCHack")

#page menu
option = st.sidebar.selectbox("Menu", ('Check Balance','Deposit Check', 'Get Cash'))
##current page title
st.header(option)

if option == 'Deposit Check':
    check_image = st.file_uploader('Please Upload a Picture of your', type=["png","jpg","jpeg"])
    checkTotal = st.text_input("Enter Check Amount", value= '$', max_chars=None, key=None, type='default')
    if st.button("Confirm"):
        st.balloons()
        if st.success("Success"):
            st.write("Check Deposit Confirmed: ", checkTotal," , Please allow for 2-3 business days for full transfer.")

if option == 'Check Balance':
    st.subheader("Check Balance")
    #data
    df = pd.DataFrame(np.random.randn(50,20), columns=('col %d' % i for i in range(20)))
    st.dataframe(df)

if option == 'Get Cash':
    pickUpDate = st.date_input('Enter Pick Up Date')
    pickUpTime = st.time_input('Pick Up Time')
    pickUpAmount = st.text_input("Amount", value= '$10.00', max_chars=None, key=None, type='default')
    if st.button("Confirm"):
        st.balloons()
        if st.success("Success"):
            st.write("Pickup Confirmed: ", "See you ", pickUpDate," at ",pickUpTime," for ", pickUpAmount)
   
 

