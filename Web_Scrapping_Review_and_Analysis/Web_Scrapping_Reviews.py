# Importing the Libraries required for scrapping

import requests
from bs4 import BeautifulSoup
import pandas as pd

# entering the url from which to scrape the reviews
base_url='https://www.airlinequality.com/airline-reviews/british-airways/'
pages = 20  #number of pages from which we can scrape the data
page_size =100   
reviews=[]    #List in which we will append the reviews

#Loop for extracting the reviews
for i in range(1,pages+1):
    print(f'Scrapping Page {i}')
    url = f"{base_url}/page/{i}/?sortby=post_date%3ADesc&pagesize={page_size}"

    response = requests.get(url)

    content = response.content
    parsed_content = BeautifulSoup(content,'html.parser')
    for para in parsed_content.find_all("div",{"class":"text_content"}):
        reviews.append(para.get_text())

    print(f"    ----> {len(reviews)} total reviews")
#Transforming the reviews into csv 
df = pd.DataFrame()
df["reviews"] = reviews
df.head()
# Saving the Reviews in Excel file
df.to_csv("BA_reviews.csv")
