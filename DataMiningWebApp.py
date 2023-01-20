import pandas as pd
import streamlit as st
import time
import webbrowser
from PIL import Image

st.title ("Data Science Fundementals Project: Movie Recommendation System")

df = pd.read_csv("Cleaned_Dataset.csv")

#Select Location
Select = st.radio("Please select", ( "Introduction", "Question 2", "Question 3"))


if Select == "Introduction":
    # set header
    st.header('Introduction')
    
    # set subheader
    st.markdown('In this area of moderation, with the rapid development of technology, there is a big impact on people life, especially the changes of entertainment. Entertainment is  known as one of the parts of human. Different type of entertainment got different generation. Start from 19th century, as the development of movies, there are many types of movies occur in different generation. However, not every movie is recommended to watch, because different people got different preference. In this project, I aim to use a machine learning model which is k-means to categorize each movie based on their publish year. And from here find out which year range has the highest score. K-means is one of the clustering technics which can be categorized the item based on their characteristics.')
    
  
elif Select == "Question 2":
    # set header
    st.header('Question 2: Which generation of customer spend the most time in the shop?')
    
    # set subheader
    st.subheader('Exploratory Data Analysis')
    st.markdown('First, visualize the relationship of the sales and the weather.')
    st.markdown('The first plot will be showing the sales during no rain day.')
    image = Image.open('Sales vs Date (No Rain).jpg')
    st.image(image, caption='Sales vs Date (No Rain)')
    
    st.markdown('The next plot will be showing the sales during rainny day.')
    image = Image.open('Sales vs Date (Rain).jpg')
    st.image(image, caption='Sales vs Date (Rain)')
    
    st.markdown('In order to observe the differences of the plots easilly, we combine both plot into one.')
    image = Image.open('Sales vs Date (Combine).jpg')
    st.image(image, caption='Sales vs Date (Rain)')
    st.markdown('From the graph above, we can see that there is a slight difference on the sales based on the weather, did it rain.')
    st.markdown('There is a slightly higher sales revenue when there is rain.')
    
    # set subheader
    st.subheader('Regression Model - Linear Regression')
    st.markdown('First, we construct a Linear Regression model using statemodels and the plot below is the result of it.')
    image = Image.open('Result regression model (statemodels).jpg')
    st.image(image, caption='Linear Regression model (statemodels)')
    
    st.markdown('Beside using statemodels, we also construct the Linear Regression model using sklearn.')
    image = Image.open('Result regression model (sklearn) 1.jpg')
    st.image(image, caption='Linear Regression model (sklearn)')
    image = Image.open('Result regression model (sklearn) 2.jpg')
    st.image(image, caption='Linear Regression model (sklearn)')
    
    # set subheader
    st.subheader('Regression Model - Decision Tree')
    image = Image.open('Decision Tree Regressor Result.jpg')
    st.image(image, caption='Decision Tree Regressor')
    st.markdown('Mean absolute error = 213.58')
    st.markdown('MSE :  80110.303842')
    st.markdown('RMSE :  283.037637')
    
elif Select == "Question 3":
    # set header
    st.header('Question 3: What types of customer will bring kids?')
    
    # set subheader
    st.subheader('Exploratory Data Analysis')
    st.markdown('First, we plot a bar chart to show the amount of customer who bring kids based on their races and gender.')
    image = Image.open('Customer who will bring kids.jpg')
    st.image(image, caption='Customer who will bring kids')
    st.markdown('Based on the Group Bar plot, we can find out that majority of the female, especially Malay Female like to bring kids to laundry. The amount of female malay is 457, higher than male malay. Indian female amount is 350, compare with Indian male is higher. However, when comparision between chinese male and female, chinese male amount slighty higher than chinese female. At last, Foreigner female amount is higher than foreigner male.')
    
    st.markdown('Next will be plotting a chart which shows the type of kids that a female customer bring to the laundry shop.')
    image = Image.open('Kids type that a female customer will bring.jpg')
    st.image(image, caption='Kids type that a female customer will bring')
    
    # set subheader
    st.subheader('Association Rule Minning')
    st.markdown('We also used Association Rule Minning to find out the characteristic of customer that will bring kids to the laundry shop.')
    image = Image.open('Association Rule Minning.jpg')
    st.image(image, caption='Association Rule Minning')

    # set subheader
    st.subheader('Feature Selection - Boruta')
    st.markdown('The first feature selection technique we used is Boruta Feature Selection. The plot below is showing the Boruta Features Score.')
    image = Image.open('Boruta Features Score.jpg')
    st.image(image, caption='Boruta Features Score')
    
    # set subheader
    st.subheader('Feature Selection - Information Gain')
    st.markdown('The second feature selection technique we used is Information Gain Feature Selection. The plot below is showing the Information Gain Features Score.')
    image = Image.open('Information Gain Features Score.jpg')
    st.image(image, caption='Information Gain Features Score')
    
    # set subheader
    st.subheader('Classification - SVM')
    st.markdown('Our first classification model is SVM.')
    st.markdown('We fit the model with Top 5 & 10 features (Information Gain & Boruta).')
    image = Image.open('ROC plot for SVM models.jpg')
    st.image(image, caption='ROC plot for SVM models')
    
    # set subheader
    st.subheader('Classification - KNN')
    st.markdown('Second classification model will be KNN.')
    st.markdown('We created the k-NN model with 10 neighbours and also fit the model with Top 5 & 10 features (Information Gain & Boruta).')
    image = Image.open('ROC plot for KNN models.jpg')
    st.image(image, caption='ROC plot for KNN models')
    
    # set subheader
    st.subheader('Stacked Ensemble Modeling')
    st.markdown('- Level-0 = {K-NN, SVM}')
    st.markdown('- Level-1 = SVM')
    image = Image.open('Stacked Emsemble model.jpg')
    st.image(image, caption='Stacked Emsemble model')
    
    # set subheader
    st.subheader('SMOTE')
    st.markdown('We created a KNN classifier in fit the model to SMOTE dataset & NON-SMOTE dataset in order to see the differences.')
    st.markdown('We also plotted a ROC chart to compare KNN classifier with and without SMOTE')
    image = Image.open('ROC plot for KNN with SMOTE and without SMOTE.jpg')
    st.image(image, caption='ROC plot for KNN with SMOTE and without SMOTE')
    
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////    
with open("Report.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(label="Download Report",
                    data=PDFbyte,
                    file_name="Report.pdf",
                    mime='application/octet-stream')
