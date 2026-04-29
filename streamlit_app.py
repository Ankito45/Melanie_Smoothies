# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col
import requests  
import pandas as pd


# Write directly to the app
st.title(f"🥤 Customise Your Smothie 🥤")
st.write(
  """
  Choose the fruits you want in your custom Smoothie
  """)

name_on_order = st.text_input('Name of Smoothie')
st.write('The name on your smoothies will be:', name_on_order)

cnx = st.connection("snowflake")
session = cnx.session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'), col('SEARCH_ON'))
pf_df = my_dataframe.to_pandas()

# st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list = st.multiselect(
    'Choose up to 5 ingredients:',
    my_dataframe,
    max_selections = 5
)

# New Section to display smoothiefront nutrition information
# New Section to display smoothiefront nutrition information
if ingredients_list:
    ingredients_string = ''  # Initialized with one 'i'
  
    for fruit_chosen in ingredients_list:
        # FIX 1: Use the correct variable name (remove the extra 'i')
        ingredients_string += fruit_chosen + ' ' 
        
        # FIX 2: Use pf_df (matching what you defined earlier)
        search_on = pf_df.loc[pf_df['FRUIT_NAME'] == fruit_chosen, 'SEARCH_ON'].iloc[0]
        st.subheader(fruit_chosen + ' Nutrition Information')
        # FIX 3: Use an f-string (f"...") so {search_on} is replaced by the value
        smoothiefroot_response = requests.get(f"https://my.smoothiefroot.com/api/fruit/{search_on}")
        # Display the JSON response
        st.dataframe(data=smoothiefroot_response.json(), use_container_width=True)
    
    # Move the button outside the loop so it only appears once
    time_to_insert = st.button('Submit Order')

    if time_to_insert:
        # Note: Ensure my_insert_stmt is defined before this line!
        session.sql(my_insert_stmt).collect()
        st.success(f'Your Smoothie is ordered, {name_on_order}!', icon="✅")

