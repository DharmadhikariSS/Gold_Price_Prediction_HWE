# Group 5 - Gold Price Forecasting Model (P-111)

import streamlit as st
import pandas as pd 
from statsmodels.tsa.holtwinters import Holt
from statsmodels.tsa.holtwinters import ExponentialSmoothing 
import numpy as np 
from matplotlib import pyplot as plt
import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
from matplotlib import pyplot




data = pd.read_csv("Gold_data.csv")
data2 = pd.read_csv("Gold_data.csv",header=0, index_col=0,parse_dates=True )


final_hwe =ExponentialSmoothing(data["price"],seasonal="mul",trend="mul",seasonal_periods=12).fit()



st.set_page_config(page_title='Gold Price Prediction', page_icon="🌐")
st.title("Forecasting gold price")

nav = st.sidebar.radio("Select Navigation",["Group 5 - P111", "About data","Forecast"])
if nav == "Group 5 - P111":
    st.subheader("Group 5 Members Details")
    st.write('''
    ##### Satyajeet Dharmadhikari [LinkedIn](https://www.linkedin.com/in/satyajeet-dharmadhikari/)  |  [GitHub](https://github.com/DharmadhikariSS/DharmadhikariSS)
    ##### Shubham Pawar [LinkedIn](https://www.linkedin.com/in/shubham-pawar-b4a432216)  |  [GitHub](https://github.com/shubhamkpawar7)
    ##### Harshada Shinde [LinkedIn](https://www.linkedin.com/in/harshada-shinde-a621121ba)  |  [GitHub](https://github.com/HarshadaAShinde)
    ##### Sushma Narsayya Gurrayya [LinkedIn](https://www.linkedin.com/in/sushma-narsayya-gurraya-047599181)  |  [GitHub](https://github.com/SushiN18)
    ##### Tofiqahemad Bag Shaikh [LinkedIn](https://www.linkedin.com/in/taufeeq-ahmed-a4602113b)  |  [GitHub](http://www.github.com/TaufeeqA)
    ##### Veda Gowda [LinkedIn]()  |  [GitHub](https://github.com/vedag321)
    ##### Komal Retawade [LinkedIn](https://www.linkedin.com/in/komal-retawade-550462234/)  | [GitHub](https://github.com/Retawadekomal)
    ##### Priyank Ukirade [LinkedIn](https://www.linkedin.com/in/priyank-ukirade-390329200)  |  [GitHub](https://github.com/PriyankUkirade)
    '''
    )

    
if nav == "About data":
    st.subheader("Data")
    data
    st.set_option('deprecation.showPyplotGlobalUse', False)


   

    st.subheader("Line plot of the data") 
    st.line_chart(data=data.price, width=150, height=300, use_container_width=True)

 
  
if nav == "Forecast":
    
    date = st.slider("Select number of days from 21/12/2021",1,50,step = 1)

    st.subheader("Forecasting the data for next few day")
    
    
    pred = final_hwe.forecast(date)

   
    if st.button("Predict"):
       st.subheader(f"Your predicted gold price from date 21/12/2021" )
       pred

       st.subheader("Line plot of the Forecasted data")
       st.line_chart(pred)

