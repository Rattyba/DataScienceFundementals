import pandas as pd
import streamlit as st
import time
import webbrowser
from PIL import Image

st.title ("Data Science Fundementals Project: Movie Recommendation System")

df = pd.read_csv("Cleaned_Dataset.csv")

#Select Location
Select = st.radio("Please select", ( "Introduction", "Data Preprocessing", "EDA"))


if Select == "Introduction":
    # set header
    st.header('Introduction')
    
    # set subheader
    st.markdown('In this area of moderation, with the rapid development of technology, there is a big impact on people life, especially the changes of entertainment. Entertainment is  known as one of the parts of human. Different type of entertainment got different generation. Start from 19th century, as the development of movies, there are many types of movies occur in different generation. However, not every movie is recommended to watch, because different people got different preference. In this project, I aim to use a machine learning model which is k-means to categorize each movie based on their publish year. And from here find out which year range has the highest score. K-means is one of the clustering technics which can be categorized the item based on their characteristics.')
    
  
elif Select == "Data Preprocessing":
    # set header
    st.header('Data Preprocessing')
    
   
    st.markdown('The dataset which I used for this project was get from Kaggle. The data name is movie.csv. There are 15 columns at this dataset. Which are name (String), rating (String), genre (String), year (Integer), released (String), score (float), votes (float), director (String), writer (String), star (String), country (String), budget (float), gross (float), company (String), runtime (float). But not every column will be used. I drop some unrelated columns, which are name, budget, gross, runtime, writer, star, country, company, director, rating.  After checking the whole dataset, there are some null data. So, for numerical data, I  used 0 to replace the empty value, and for categorical data, I used the word unknown to replace the empty data. ')
    image = Image.open('data_preprocessing.PNG')
    st.image(image, caption='Data Preprocessing')
    
    
elif Select == "EDA":
    # set header
    st.header('Exploratory Data Analysis')
    
    st.markdown('For the entire project, I will based on the below question to do clustering on each of the movie. ')
    image = Image.open('table.PNG')
    st.image(image, caption='The total score at each range of year of movies')
    st.markdown('From the table we can found out that the total score from 1990 until 2000 and 2000 until 2010 is 2000.')
    
    image = Image.open('barchart.PNG')
    st.image(image, caption='Bar Chart for different movies total score in each range of year')
    st.markdown('Based on the bar chart which showed at top, I can found out that the range between 1990 until 2000 and range between 2000 until 2010 have the highest score based on their movies total score. The score of both ranges got is 2000. The columns that I used for this bar chart is year and score. ')
    
   
    
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////    
with open("Report.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(label="Download Report",
                    data=PDFbyte,
                    file_name="Report.pdf",
                    mime='application/octet-stream')
