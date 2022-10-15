from asyncore import write
from distutils.command.clean import clean
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from joblib import load
from PIL import Image
def load_model():
    return load('Model/housing_model.jb')
st.set_page_config(
    page_title="House Price Prediction",
    layout='centered',
    page_icon="🛃"
)
def introduction():
    # st.image('vg.gif', width=None)
    st.markdown("""
        
    Name : Prajjwal Singh
    \nQualification : Bachelor ofComputer Application(BCA)
    \nStream : Computer Science
    \nUniversity : University of Lucknow
    \nLocation : Lucknow, INDIA
    \nThis Project Perfrom Prdiction Wheather You Have Donated Blood Or not 
        
        - The Libraries I used in Project are:
            Matplotlib Explore here
            Sklearn Explore Here
            Streamlit Explore here
            Pandas 
            imbelearn 
        - Their Following Tasks are Implemented in the Project:
            Data Preparation and Cleaning
            Model design
            Best Feature Selectio 
            References and Future Work
    """)
    st.markdown("**Datset used**")
    st.caption("Datset used")
 
    df=load('Model/original_data.jb')
    # df=pd.read_csv(url)
    st.write(df)
    st.write("DAta Used FOr Maximum Accuracy:")
    clean_data=load('Model/data.jb')
    st.write(clean_data)
    st.caption("About The Data")
    st.write(	
        '''OverallQual: Rates the overall material and finish of the house

       10	Very Excellent
       9	Excellent
       8	Very Good
       7	Good
       6	Above Average
       5	Average
       4	Below Average
       3	Fair
       2	Poor    
       1	Very Poor''')
    st.write("YearBuilt: Original construction date")
    st.write("TotalBsmtSF: Total square feet of basement area")
    st.write("1stFlrSF: First Floor square feet")
    st.write("GrLivArea: Above grade (ground) living area square feet")
    st.write("FullBath: Full bathrooms above grade")
    st.write("TotRmsAbvGrd: Total rooms above grade (does not include bathrooms)")
    st.write("GarageCars: Size of garage in car capacity")
    st.write("GarageArea: Size of garage in square feet")
    st.write('''KitchenQual: Kitchen quality


       
        Ex	Excellent
       Gd	Good
       TA	Typical/Average
       Fa	Fair
       Po	Poor''')

    st.write('''BsmtQual: Evaluates the height of the basement


        Ex	Excellent (100+ inches)	
       Gd	Good (90-99 inches)
       TA	Typical (80-89 inches)
       Fa	Fair (70-79 inches)
       Po	Poor (<70 inches
       NA	No Basement''')

    st.write('''Foundation: Type of foundation

		
       BrkTil	Brick & Tile
       CBlock	Cinder Block
       PConc	Poured Contrete	
       Slab	Slab
       Stone	Stone
       Wood	Wood''')
    st.write('''
        ExterQual: Evaluates the quality of the material on the exterior 

		
       Ex	Excellent
       Gd	Good
       TA	Average/Typical
       Fa	Fair
       Po	Poor''')
    
    st.write('''
    GarageFinish: Interior finish of the garage


       Fin	Finished
       RFn	Rough Finished	
       Unf	Unfinished
       NA	No Garage''')
def execute():
    result=0.8593430129872129
    non_result=1-result
    legend=["Accuracy","Not Accurate"]
    sizes = np.array([result,non_result])
    fig1, ax1 = plt.subplots(figsize=(5,5))
    colour=["blue","purple"]
    # colour=["black","grey"]
    ax1.pie(sizes, labels=legend, colors=colour,autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.sidebar.write("The Maximum Accuracy Of the Model is :85.9%")
    st.sidebar.pyplot(fig1, )
    with st.form("form1",clear_on_submit=True):
        df=load('Model/data.jb')
        # st.write("The MAximum Accuracy Of the Model is :87%")
        OverallQual=st.number_input("OverallQual: Rates the overall material and finish of the house",min_value=0,max_value=10,step=1)
        YearBuild=st.number_input("YearBuilt: Original construction date",min_value=1900,max_value=2050,step=20)
        YearRemodAdd=st.number_input("YearRemodAdd: Remodel date of the House",min_value=1900,max_value=2050,step=20)
        TotalBsmtSF=st.number_input("TotalBsmtSF: Total square feet of basement area",min_value=0,max_value=2000,step=20)
        first_FlrSF=st.number_input("1stFlrSF: First Floor square feet",min_value=0,max_value=2000,step=20)
        GrLivArea=st.number_input(" GrLivArea: Above grade (ground) living area square feet",min_value=0,max_value=2000,step=20)
        FullBath=st.number_input("FullBath: Full bathrooms above grade",min_value=0,max_value=10,step=20)
        TotRmsAbvGrd=st.number_input("TotRmsAbvGrd: Total rooms above grade (does not include bathrooms)",min_value=0,max_value=10,step=1)
        GarageCars=st.number_input("GarageCars: Size of garage in car capacity",min_value=0,max_value=10,step=1)
        GarageArea=st.number_input("GarageArea: Size of garage in square feet",min_value=0,max_value=700,step=20)
        ExterQual=st.selectbox('ExterQual: Evaluates the quality of the material on the exterior',df['ExterQual'].unique())
        Foundation=st.selectbox('Foundation: Type of foundation',df['Foundation'].unique())
        BsmtQual=st.selectbox('BsmtQual: Evaluates the height of the basement',df['BsmtQual'].unique())
        GarageFinish=st.selectbox('GarageFinish: Interior finish of the garage',df['GarageFinish'].unique())
        KitchenQual=st.selectbox('KitchenQual: Kitchen quality',df['KitchenQual'].unique())
        btn = st.form_submit_button("Predict Prices")
        if btn:
            model=load_model()
            result=np.array([OverallQual, YearBuild, YearRemodAdd, TotalBsmtSF,first_FlrSF, GrLivArea,FullBath, TotRmsAbvGrd, GarageCars, GarageArea, ExterQual, Foundation, BsmtQual, KitchenQual, GarageFinish])
            result=pd.DataFrame(result).T
            result=result.rename(columns={0:"OverallQual",1:"YearBuilt"	,2:"YearRemodAdd",	3:"TotalBsmtSF"	,4:"1stFlrSF",5:"GrLivArea"	,6:"FullBath"	,7:"TotRmsAbvGrd",	8:"GarageCars",	9:"GarageArea",10:"ExterQual",11:"Foundation",12:"BsmtQual",13:"KitchenQual",14:"GarageFinish"})
            
            print(model.predict(result))
            # st.title(model.predict([result]))
            answer=int(model.predict(result))
           
            st.write("The Price Of the House is :",answer)

image=Image.open("house_sale.jpg")

st.header("House Price Prediction ")

options = ['Project Introduction', 'Execution']

sidebar = st.sidebar

sidebar.title('User Options')

selOption = sidebar.selectbox("Select an Option", options)

if selOption == options[0]:
    introduction()
elif selOption == options[1]:
    execute()
        
