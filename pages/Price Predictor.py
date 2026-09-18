from sys import base_exec_prefix

import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.set_page_config(page_title="Price Pridiction")

with open("df.pkl", "rb")  as file:
    df= pickle.load(file)

with open("pipeline.pkl", "rb")  as file:
    pipeline= pickle.load(file)



st.header("Enter your inputs")

property_type = st.selectbox("Property type",["flat","house"])
sector = st.selectbox("sector",sorted(df["sector"].unique().tolist()))

bedrooms = float(st.selectbox("Number of Bedroom",sorted(df["bedRoom"].unique().tolist())))
bathroom = float(st.selectbox("Number of Bathroom",sorted(df["bathroom"].unique().tolist())))
balcony = st.selectbox("Balconies",sorted(df["balcony"].unique().tolist()))
property_age = st.selectbox("Property Age",sorted(df["agePossession"].unique().tolist()))
built_up_area  = float(st.number_input("Built Up Area"))

servent_room = float(st.selectbox("Servent Room",[0.0,0.1]))
store_room = float(st.selectbox("Store Room",[0.0,0.1]))

furnhising = st.selectbox("Furnhising Type",sorted(df["furnishing_type"].unique().tolist()))
luxury_category = st.selectbox("Luxury Category",sorted(df["luxury_category"].unique().tolist()))
floor_category= st.selectbox("Floor Category",sorted(df["floor_category"].unique().tolist()))

if st.button("predict"):
    # from a dataframe
    data = [[property_type, sector, bedrooms, bathroom, balcony, property_age, built_up_area, servent_room,
             store_room, furnhising, luxury_category, floor_category]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
               'agePossession', 'built_up_area', 'servant room',
                'store room','furnishing_type', 'luxury_category', 'floor_category']

    # convert to dataframe
    one_df = pd.DataFrame(data, columns=columns )
    # st.dataframe(one_df)

    #predict
    base_price = np.expm1(pipeline.predict(one_df))[0]
    low = base_price - 0.22
    high = base_price + 0.22

    # display
    st.text("The price of flat is between {} Cr and {} Cr".format(round(low,2), round(high,2)))
