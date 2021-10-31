import streamlit as st
import pandas as pd
import numpy as np
import requests


#########
###########



url = 'http://api.nessieisreal.com/customers?key=da4f6777887367bc27414d3d13157abe'
IMGurl = 'https://media.discordapp.net/attachments/903431149412548672/904380213910200321/Add_a_subheading-3.png'

visa_url = "https://sandbox.api.visa.com/globalatmlocator/v1/localatms/atmsinquiry"

#page title
st.sidebar.subheader("HackUMBC 2021")
st.sidebar.image(IMGurl)

user = "John Doe"
#page menu
st.sidebar.write("Welcome ", user, ",")
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
    st.text("Would you like to check your balance?")
    if st.checkbox("Show Current Balance"):
        balance = 10,590.34
        st.write("$", balance)
        if st.checkbox("Show Recent Transactions"):
            #data
            an_array = np.array([['Macbook Pro Laptop','$1700.00', '12/30/19 00:01', '136 Church St, New York City, NY 10001'],['LG Washing Machine','$600.00', '12/29/19 07:03', '562 2nd St, New York City, NY 10001'],['USB-C Charging Cable','$11.59', '12/12/19 18:21', '277 Main St, New York City, NY 10001'],['27in FHD Monitor','$149.99', '12/22/19 15:13', '410 6th St, San Francisco, CA 94016']])
            ser = pd.DataFrame(an_array,
                index = [1,2,3,4],
                columns= ['Transactions', 'Price Each', 'Order Date', 'Purchase Address'])
            df = pd.DataFrame(np.random.randn(50,20), columns=('col %d' % i for i in range(20)))
            st.dataframe(ser)

if option == 'Get Cash':
    pickUpDate = st.date_input('Enter Pick Up Date')
    pickUpTime = st.time_input('Pick Up Time')
    pickUpAmount = st.text_input("Amount", value= '$10.00', max_chars=None, key=None, type='default')
    if st.checkbox("Find Nearest Location"):
        st.map()
    if st.button("Confirm"):
        st.balloons()
        if st.success("Success"):
            st.write("Pickup Confirmed: ", "See you ", pickUpDate," at ",pickUpTime," for ", pickUpAmount)
   
 

