import streamlit as st

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from PIL import Image


st.sidebar.title("Tesla Customer Satisfaction Analysis from Reddit")
# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Pages",
        ("Models Info", "Reddit Comments Analysis", "Sentiment Analysis", "Word Cloud", "Business Recommendations")
    )


if (add_radio == 'Models Info'):
	st.title('Tesla Models')

	col1, col2, col3  = st.columns(3)

	with col1:
	    st.header("Model S")
	    st.write("Luxury Sedan  --  $97k")
	    st.image("https://i.imgur.com/bOeGXlf.jpeg", width= 400)

	with col2:
	    st.write(" ")

	with col3:
	    st.header("Model 3")
	    st.write("Affordable Sedan  --  $45k")
	    st.image("https://i.imgur.com/oxo1qMF.jpeg", width= 400)


	col1, col2, col3 = st.columns(3)

	with col1:
	    st.header("Model X")
	    st.write("Luxury SUV  --  $107k")
	    st.image("https://i.imgur.com/lpVEGrH.jpeg", width= 400)

	with col2:
	    st.write(" ")

	with col3:
	    st.header("Model Y")
	    st.write("Affordable SUV  --  $58k")
	    st.image("https://i.imgur.com/9bzOyOU.jpeg", width= 400)


	# with col1:
	option = st.selectbox(
	     'Select for specification details',
	     ('Select here','Model S', 'Model 3', 'Model X', 'Model Y'))
	if (option != 'Select here'):
	    st.write( 'Details for ', option ,':-')
	if (option == 'Model S'):
	    st.write('Range : 396mi')
	    st.write('0-60 : 1.99s')
	    st.write('Top Speed : 200mph')
	    st.write('Peak Power : 1020hp')
	if (option == 'Model 3'):
	    st.write('Range : 358mi')
	    st.write('0-60 : 3.1s')
	    st.write('Top Speed : 162mph')
	    st.write('Peak Power : 450hp')
	if (option == 'Model X'):
	    st.write('Range : 333mi')
	    st.write('0-60 : 2.5s')
	    st.write('Top Speed : 163mph')
	    st.write('Peak Power : 1020hp')
	if (option == 'Model Y'):
	    st.write('Range : 330mi')
	    st.write('0-60 : 3.5s')
	    st.write('Top Speed : 155mph')
	    st.write('Peak Power : 450hp')

	st.image("https://imgur.com/Ua0MQoa.jpeg", width= 900)




if (add_radio == 'Reddit Comments Analysis'):
	# Set some default options
	pd.set_option('display.max_columns', None)
	pd.set_option('display.max_rows', 100)
	sns.set_style('darkgrid')
	plt.rc('figure', facecolor='#00000000', figsize=(10,8))
	plt.rc('font', size=12)


	df = pd.read_csv('/Users/abhi/Downloads/TeslaData.csv')

	df.drop(columns=['MsgID', 'ThreadID', 'ReplyTo', 'Author'], inplace=True)


	df['Timestamp'] =  pd.to_datetime(df['Timestamp'], infer_datetime_format=True, format='%Y-%m-%d %H:%M:%S')

	# Extract year and month of the data
	df['year'] = pd.DatetimeIndex(df['Timestamp']).year
	df['month'] = pd.DatetimeIndex(df['Timestamp']).month

	st.set_option('deprecation.showPyplotGlobalUse', False)

	

	st.header("Posts and Comments by Year and Month")
	
	st.write(" ")
	st.write(" ")

	col1, col2 = st.columns(2)
	with col1:
		# Create a count plot
		sns.countplot(x='year', data=df)
		plt.title('Number of posts and comments by year')
		st.pyplot()


	st.write(" ")
	st.write(" ")
	st.write(" ")
	st.write(" ")

	with col2:
		sns.countplot(x='month', data=df.loc[df['year'] == 2021])
		plt.title('Number of posts and comments by month (2021)')
		st.pyplot(width = 200)
		

	st.write(" ")
	st.write(" ")
	st.write(" ")
	st.write(" ")
	st.write(" ")
	

	st.image("https://imgur.com/E6xs0kK.jpeg", width= 600)

		

if (add_radio == 'Sentiment Analysis'):


	header = st.container()
	dataset =  st.container()
	features = st.container()
	model_training = st.container()

		# Using object notation
	
	add_selectbox = st.selectbox(
	    "Choose:",
	    ("Happy Transformer", "Text Blob", "VADER")
	)


	if(add_selectbox == "Happy Transformer"):
		st.title('Sentiment Analysis : Happy Transformer')
		st.image("https://imgur.com/b5DfxAV.jpeg", width= 900)
		st.write("When manually researching these comments, most of the comments are actually positive or neutral")

	

	if(add_selectbox == "Text Blob"):

		st.title('Classifier : Text Blob')
		st.write('Model 3 and Model Y have a higher proportion of positive reviews')
		st.image("https://imgur.com/GOoYxB0.jpeg", width= 500)
		st.image("https://imgur.com/xdVDIuG.jpeg", width= 700)
		st.write("It's clear that people don't choose to buy Tesla's luxury SUV models over other models, as the Model X has far fewer reviews than other models")

	if(add_selectbox == "VADER"):

		st.title('Sentiment Analysis : VADER')
		st.image("https://imgur.com/1w56srM.jpeg", width= 900)
		st.write("Autopilot and after-sales service are representative features of Tesla, and based on VADER sentiment analysis, the responses are truly great")



if (add_radio == 'Word Cloud'):
	add_selectbox = st.selectbox(
		"Choose:",
		("Overall Comments","Positive Reviews contain 'AUTOPILOT'","Comments contain 'SERVICE'"))

	if(add_selectbox == "Overall Comments"):
		st.image("https://imgur.com/nNL2pG9.jpeg", width= 900)

	if(add_selectbox == "Positive Reviews contain 'AUTOPILOT'"):
		st.image("https://imgur.com/mSNpbu2.jpeg", width= 900)

	if(add_selectbox == "Comments contain 'SERVICE'"):
		st.image("https://imgur.com/t2zZ5oH.jpeg", width= 900)


if (add_radio == 'Business Recommendations'):
	st.title("Business Recommendations")
	st.subheader("Target Model")
	st.write("In general, Model 3 is indeed a relatively painless starting model, with the most basic equipment but the highest cost - performance ratio")
	st.subheader("Features focusing")
	st.write("Having a high percentage of praise fully reflects Tesla‘s success in autopilot, and Tesla should continue to be at the forefront of this field")
	st.subheader("Price & Policy")
	st.write("Price is subjective, but good after-sales service can increase customer loyalty, or occasionally going crazy like sending a lifetime supercharger")