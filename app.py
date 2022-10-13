import streamlit as st
import numpy as np
import pandas as pd
from joblib import load
from PIL import Image
def load_model():
    return load('model/housing_model.jb')
st.set_page_config(
    page_title="Blood Donation Camp",
    layout='centered',
    page_icon="🛃"
)
# image=Image.open("blood.png")
# st.image(image,width=100,caption='Sunrise by the mountains')
st.header("House Rate")
with st.form("form1",clear_on_submit=True):
    df=load('model/data.jb')
    OverallQual=st.number_input("erallQual(months since the last donation)",min_value=0,max_value=10,step=1)
    YearBuild=st.number_input("YearBuild(total number of donation)",min_value=1900,max_value=2050)
    YearRemodAdd=st.number_input("Monerty ( total blood donated in c.c)",min_value=1900,max_value=2050)
    TotalBsmtSF=st.number_input(" TotalBsmtS(months since the first donation)",min_value=0,max_value=2000)
    first_FlrSF=st.number_input(" first_FlrSF(months since the first donation)",min_value=0,max_value=2000)
    GrLivArea=st.number_input(" GrLivArea(months since the first donation)",min_value=0,max_value=2000)
    FullBath=st.number_input("FullBat(months since the first donation)",min_value=0,max_value=10)
    TotRmsAbvGrd=st.number_input("TotRmsAbvGrd(months since the first donation)",min_value=0,max_value=10)
    GarageCars=st.number_input("GarageCars(months since the first donation)",min_value=0,max_value=10)
    GarageArea=st.number_input("GarageArea(months since the first donation)",min_value=0,max_value=700)
    ExterQual=st.selectbox(' ExterQual',df['ExterQual'].unique())
    Foundation=st.selectbox('Foundation',df['Foundation'].unique())
    BsmtQual=st.selectbox('BsmtQual',df['BsmtQual'].unique())
    GarageFinish=st.selectbox('GarageFinish',df['GarageFinish'].unique())
    KitchenQual=st.selectbox('KitchenQual',df['KitchenQual'].unique())
    btn = st.form_submit_button("Predict Prices")
    if btn:
        model=load_model()
        result=np.array([OverallQual, YearBuild, YearRemodAdd, TotalBsmtSF,first_FlrSF, GrLivArea,FullBath, TotRmsAbvGrd, GarageCars, GarageArea, ExterQual, Foundation, BsmtQual, KitchenQual, GarageFinish])
        result=pd.DataFrame(result).T
        result=result.rename(columns={0:"OverallQual",1:"YearBuilt"	,2:"YearRemodAdd",	3:"TotalBsmtSF"	,4:"1stFlrSF",5:"GrLivArea"	,6:"FullBath"	,7:"TotRmsAbvGrd",	8:"GarageCars",	9:"GarageArea",10:"ExterQual",11:"Foundation",12:"BsmtQual",13:"KitchenQual",14:"GarageFinish"})
        print("Hello")
        print("Hello")
        print("Hello")
        print(result)
        print("workin")
        print("workin")
        print("workin")
        print("workin")
        print(model.predict(result))
        # st.title(model.predict([result]))
        answer=int(model.predict(result))
        print(answer)
        print("answer")
        print("answer")
        print("answer")
        print("answer")
        st.write(answer)
        # if answer==1:
        #     st.error('Please Donate Blood', icon="🚨")
            
        # else:
        #     st.success("Thank You For Donating Blood",icon="✅")
        # st.title("The predicted price of this configuration is "+ str(answer))
        # ans=model.predict([result])
        # st.write(model.predict([result]))
