import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
import seaborn as sns
sns.set()

import mysql.connector as connection

mydb = connection.connect(
    host="relational.fit.cvut.cz",
    user="guest",
    password="relational",
    database="CraftBeer"
)

#Read SQL querry or database into python
df = pd.read_sql_query('SELECT * FROM CraftBeer.breweries', mydb)
py = pd.read_sql_query('SELECT * FROM CraftBeer.beers', mydb)




query = "SELECT beer_name, brewery, rating FROM craft_beers"

img = Image.open('brew.jpg')
st.image(img.resize((4000,2000)))
#a subheader with title name
st.title("Chidavisa Beer Hub")

st.subheader("Craft Beer Data, drink responsibly!!!")
st.dataframe(df)



#displaying select bar where breweries details such as name, location and id can be found

st.sidebar.title('Craft breweries')
breweries= st.sidebar.selectbox('Select Brewery Name', df['name'].unique())
filtered_df = df[(df['name'] == breweries)]

st.write(filtered_df)

filtered_beers = py[(py['style'] == breweries)]

# Bar chart of beer styles
fig, ax = plt.subplots(figsize=(10, 6))
style_counts = py['style'].value_counts()
ax.bar(style_counts.index, style_counts.values)
ax.set_xlabel('Beer Style')
ax.set_ylabel('Count')
ax.set_title('Beer Styles Distribution')
st.pyplot(fig)

# Histogram of beer ABV (Alcohol by Volume)
fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(py['abv'], bins=20)
ax.set_xlabel('ABV')
ax.set_ylabel('Count')
ax.set_title('ABV Distribution')
st.pyplot(fig)

# Scatter plot of beer ratings
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(py['name'], py['abv'])
ax.set_xlabel('Name')
ax.set_ylabel('ABV')
ax.set_title('Rating vs ABV')
st.pyplot(fig)


#displaying beer names and ABV (Alcohol by Volume) from the Craftbeer dataset and also IBU stands for International Bitterness Units. It is a measurement used to quantify the bitterness of beer, specifically related to the presence of hops.

st.sidebar.title("Beer Data")
beer_selection = st.sidebar.selectbox("Select a Beer", py['name'])
selected_beer = py[py['name'] == beer_selection]


if not selected_beer.empty:
    st.sidebar.subheader("Selected Beer Composition")
    st.sidebar.write("Name:", selected_beer['name'].values[0])
    st.sidebar.write("ABV:", selected_beer['abv'].values[0])
    st.sidebar.write("IBU:", selected_beer['ibu'].values[0])
    st.sidebar.write("STYLE:", selected_beer['style'].values[0])
    st.sidebar.write("OUNCES:", selected_beer['ounces'].values[0])



# Display a section for placing an order
st.subheader("Place an Order")
# Input fields for customer details

beer_menu_data = {
    'beer_name': ['Beer 1', 'Beer 2', 'Beer 3'],
    'price': [5.99, 6.99, 7.99]
}

beer_menu = pd.DataFrame(beer_menu_data)

beer_selection = st.write("Beer Name:", selected_beer['name'].values[0])
quantity = st.number_input("Quantity:", min_value=1, value=1)
name = st.text_input("Customer Name:")

# Submit button to place the order

# Process the order when the submit button is clicked

address = st.text_input('Address:')
phone = st.text_input('Phone Number:')
submit = st.button('Submit')
if submit:
    st.write('Thank you for your order. We will contact you shortly.')
    
st.header('Contact Information')
st.write('Phone: 0806-753-3636')
st.write('Email: info@craftbeer.com')
st.write('Address: House1, Motl Avenue, Chicago USA.')

