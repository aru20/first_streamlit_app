
import streamlit
import pandas
streamlit.title('My First App')
streamlit.title('My Parent\'s New Healthy Dinner🍽️')
streamlit.header('🥗 Breakfast Menu')
streamlit.text('Smoothie')
streamlit.text('Oatmeal')
streamlit.text('Egg')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
# read csv
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# After pulling the data into a pandas dataframe called my_fruit_list, we will ask the streamlit library to display it on the page
sreamlit.dataframe(my_fruit_list)
# Let's put a pick list here so they can pick the fruit they want to include
streamlit.multiselect("pick some fruits:" ,list(my_fruit_list.index))
#display the table on the page
straemlit.dataframe(my_fruit_list)
                  
