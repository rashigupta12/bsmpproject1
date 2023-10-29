import streamlit as st
import pickle
import pandas as pd
import numpy as np

pipe = pickle.load(open('pipe.pkl','rb'))

fat = ['Item_Fat_Content_0', 'Item_Fat_Content_1']
location_type = ['Outlet_Location_Type_0', 'Outlet_Location_Type_1',
       'Outlet_Location_Type_2']
outlet_size = ['Outlet_Size_0', 'Outlet_Size_1',
       'Outlet_Size_2', 'Outlet_Size_3']
outlet_type = ['Outlet_Type_0', 'Outlet_Type_1',
       'Outlet_Type_2', 'Outlet_Type_3']
item_type = ['Item_Type_Combined_0',
       'Item_Type_Combined_1', 'Item_Type_Combined_2']
outlet_no = ['Outlet_0', 'Outlet_1',
       'Outlet_2', 'Outlet_3', 'Outlet_4', 'Outlet_5', 'Outlet_6', 'Outlet_7',
       'Outlet_8', 'Outlet_9']

st.title('Big Mart Sales Prediction')

col9, col10, col11, col12 = st.columns(4)
with col9:
       Outlet_Size = st.selectbox('Select Outlet Size', outlet_size)
with col10:
       Outlet_Type = st.selectbox('Select Outlet Type', outlet_type)
with col11:
       Item_Type = st.selectbox('Select Item Type', item_type)
with col12:
       Outlet_No = st.selectbox('Select Outlet Number', outlet_no)

col1, col2, col3, col4 = st.columns(4)

with col1:
    Item_Weight = st.number_input('Enter Item Weight')
with col2:
       Item_Visibility = st.number_input('Enter Item Visibility(%)')
with col3:
       Item_MRP = st.number_input('Enter MRP')
with col4:
       Outlet_Establishment_Year = st.number_input('Enter Estd Year')


col5, col6, col7, col8 = st.columns(4)

with col5:
       Item_Visibility_MeanRatio = st.number_input('Item visibility mean percentage')
with col6:
       Outlet_Years = st.number_input('Enter No. of year since it is operated')
with col7:
       Fat = st.selectbox('Select Item Fat Content Type', fat)
with col8:
       Location_Type =st.selectbox('select Location Type', location_type )

if st.button('Predict Sales'):
       Item_Visibility = Item_Visibility/100
       Item_Visibility_MeanRatio = Item_Visibility_MeanRatio/100

       Outlet_Size_0 = 0
       Outlet_Size_1 = 0
       Outlet_Size_2 = 0
       Outlet_Size_3 = 0

       if Outlet_Size == "Outlet_Size_0":
           Outlet_Size_0 += 1
       if Outlet_Size == "Outlet_Size_1":
           Outlet_Size_1 += 1
       if Outlet_Size == "Outlet_Size_2":
           Outlet_Size_2 += 1
       if Outlet_Size == "Outlet_Size_3":
           Outlet_Size_3 += 1

       Outlet_Type_0 = 0
       Outlet_Type_1 = 0
       Outlet_Type_2 = 0
       Outlet_Type_3 = 0

       if Outlet_Type == 'Outlet_Type_0':
           Outlet_Type_0 += 1
       if Outlet_Type == 'Outlet_Type_1':
           Outlet_Type_1 += 1
       if Outlet_Type == 'Outlet_Type_2':
           Outlet_Type_2 += 1
       if Outlet_Type == 'Outlet_Type_3':
           Outlet_Type_3 += 1

       Item_Type_Combined_0 = 0
       Item_Type_Combined_1 = 0
       Item_Type_Combined_2 = 0

       if Item_Type == 'Item_Type_Combined_0':
           Item_Type_Combined_0 += 1
       if Item_Type == 'Item_Type_Combined_1':
           Item_Type_Combined_1 += 1
       if Item_Type == 'Item_Type_Combined_2':
           Item_Type_Combined_2 += 1

       Outlet_0 = 0
       Outlet_1 = 0
       Outlet_2 = 0
       Outlet_3 = 0
       Outlet_4 = 0
       Outlet_5 = 0
       Outlet_6 = 0
       Outlet_7 = 0
       Outlet_8 = 0
       Outlet_9 = 0

       if Outlet_No == 'Outlet_0':
           Outlet_0 += 1
       if Outlet_No == 'Outlet_1':
           Outlet_1 += 1
       if Outlet_No == 'Outlet_2':
           Outlet_2 += 1
       if Outlet_No == 'Outlet_3':
           Outlet_3 += 1
       if Outlet_No == 'Outlet_4':
           Outlet_4 += 1
       if Outlet_No == 'Outlet_5':
           Outlet_5 += 1
       if Outlet_No == 'Outlet_6':
           Outlet_6 += 1
       if Outlet_No == 'Outlet_7':
           Outlet_7 += 1
       if Outlet_No == 'Outlet_8':
           Outlet_8 += 1
       if Outlet_No == 'Outlet_9':
           Outlet_9 += 1

       Item_Fat_Content_0 = 0
       Item_Fat_Content_1 = 0

       if Fat == 'Item_Fat_Content_0':
           Item_Fat_Content_0 += 1
       if Fat == 'Item_Fat_Content_1':
           Item_Fat_Content_1 += 1

       Outlet_Location_Type_0 = 0
       Outlet_Location_Type_1 = 0
       Outlet_Location_Type_2 = 0

       if Location_Type == 'Outlet_Location_Type_0':
           Outlet_Location_Type_0 += 1
       if Location_Type == 'Outlet_Location_Type_1':
           Outlet_Location_Type_1 += 1
       if Location_Type == 'Outlet_Location_Type_2':
           Outlet_Location_Type_2 += 1


       input_df = pd.DataFrame(
              {'Item_Weight': [Item_Weight],
               'Item_Visibility': [Item_Visibility],
               'Item_MRP': [Item_MRP],
               'Outlet_Establishment_Year': [Outlet_Establishment_Year],
               'Item_Visibility_MeanRatio': [Item_Visibility_MeanRatio],
               'Outlet_Years': [Outlet_Years],
               'Item_Fat_Content_0': [Item_Fat_Content_0],
               'Item_Fat_Content_1': [Item_Fat_Content_1],
               'Outlet_Location_Type_0': [Outlet_Location_Type_0],
               'Outlet_Location_Type_1': [Outlet_Location_Type_1],
               'Outlet_Location_Type_2': [Outlet_Location_Type_2],
               'Outlet_Size_0': [Outlet_Size_0],
               'Outlet_Size_1': [Outlet_Size_1],
               'Outlet_Size_2': [Outlet_Size_2],
               'Outlet_Size_3': [Outlet_Size_3],
               'Outlet_Type_0': [Outlet_Type_0],
               'Outlet_Type_1': [Outlet_Type_1],
               'Outlet_Type_2':  [Outlet_Type_2],
               'Outlet_Type_3': [Outlet_Type_3],
               'Item_Type_Combined_0': [Item_Type_Combined_0],
               'Item_Type_Combined_1': [Item_Type_Combined_1],
               'Item_Type_Combined_2': [Item_Type_Combined_2],
               'Outlet_0': [Outlet_0],
               'Outlet_1': [Outlet_1],
               'Outlet_2': [Outlet_2],
               'Outlet_3': [Outlet_3],
               'Outlet_4': [Outlet_4],
               'Outlet_5': [Outlet_5],
               'Outlet_6': [Outlet_6],
               'Outlet_7': [Outlet_7],
               'Outlet_8': [Outlet_8],
               'Outlet_9': [Outlet_9]
       })
       st.table(input_df)
       result = pipe.predict(input_df)
       st.header("Projected Sales: " + str(int(result[0])))
