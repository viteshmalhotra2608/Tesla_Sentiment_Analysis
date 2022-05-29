# Tesla_Sentiment_Analysis

Microsoft Engage 2022 Submission by Abhigyan Bajpai (abhigyanbajpai13@gmail.com)

## Introduction

This project is based on the Data Analysis Problem Statement which stated to demonstrate how the Automotive Industry could harness data to take informed decisions.

This Project aims to Extract Customer Posts and Comments from Reddit under the subreddit "Tomorrowland" and Preprocess the data. Sentiment Analysis is performed to analyse the customer behaviour towards the new features in the cars, after sales service etc. This analysis will help the company to take informed decisions and alter their plan of action to satisfy customer needs as well as improve their operations which will drive better business.


## Contents


### Images Folder

This folder contains the plots and diagrams which are used on the websites. The images used have been uploaded on https://imgur.com/upload and links for the same has been used.


### Data_Scraping_Reddit.ipynb

This is the jupyter notebook which contains the code to scrap data from the subreddit "Tomorrowland". Reddit's API has been used to extract the comments and posts of the Reddit users. The extracted data has been used to finally generate the csv dataset (Scraped_Tesla_Data_Reddit.csv).


### Data_cleaned.csv

This is the cleaned dataset after text preprocessing which has been further used for sentiment analysis.


### Scraped_Tesla_Data_Reddit.csv

This is the Raw Dataset which has been extracted from reddit by using Data Scraping Techniques.


### Sentiment_Analysis_of_Tesla.ipynb
This is the main Jupyter Notebook which preprocesses the dataset and performs sentiment Analysis on the same.


### Website.py

This is the python file which contains the code of the website.

To host the website follow the below steps

1. download the python file.
2. Open the terminal.
3. Run the command "pip install streamlit".
4. Then change the directory to where the python file is downloaded.
5. Run the command "streamlit run myfile.py". (where myfile is the name of the file)
6. The Website will be locally hosted in the web browser


### requirements.txt

This file contains all the dependencies required to run the project.
On the terminal write the command "pip install -r requirements.txt", this will install all the necessary dependencies.
