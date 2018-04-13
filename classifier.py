# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 13:37:36 2018

@author: Awal
"""

#     IMPORTING LIBRARIES AND HEADER FILES


import tweepy
from tweepy import OAuthHandler
import numpy
from textblob import TextBlob
import csv
import re
import pandas as pd
#import matplotlib
import matplotlib.pyplot as plt
#import pickle

#AUTHENTICATION OF TWITTER API 

consumer_key = 'PwP7TRcyZfl4SnqEBVJSMKa6w'
consumer_secret = '3B6NnACsu22xf78BnJNVssOittaN8c0XNbVZMfyppgq9FbStV0'
access_token = '622721291-lAeWJ46G9T8sVNoCRjngZFkzAABLnnkYV6UktVmq'
access_secret = 'b42UAgFQ503Wqe8CdO7pX6jb39nkx0hOdgXeoCbJp0tF3'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)



#   GETTING INPUT FROM USER AND FETCHING TWEETS ACCORDINGLY


twt=[]
rate=api.rate_limit_status()
print("**** Welcome to SENTIMENT ANALYSIS by Awal ****")
print("Enter 1 to search by hashtag. \nEnter 2 to search by user's screen name.\nEnter 3 for admin's tweets.")
choice=int(input())

if(choice==1):
    
    query=input("Enter the hashtag you want to perform sentiment analysis on(ex:#India):")
    results=tweepy.Cursor(api.search,q=query,tweet_mode='extended').items(100)
   


if(choice==2):
    query=input("Enter the Screen name of user you want to perform sentiment analysis on(ex:RobertDowneyJr):")
    results=tweepy.Cursor(api.user_timeline,screen_name=query,tweet_mode='extended').items(100)
if(choice==3):
    results=tweepy.Cursor(api.user_timeline,tweet_mode='extended').items(100)
    
#PROCESSING TWEETS AND STORING IT IN A CSV FILE


for status in results:
    #print(status)
    a=((status.full_text).encode("utf-8"))
    twt.append(a)    
    

polar=numpy.empty(100,dtype=float)
result=numpy.empty(100,dtype="S10")

with open('tweet.csv', "w") as data:
    out = csv.writer(data, lineterminator='\n')
    for val in twt:
        out.writerow([val])    




""""USING TEXTBLOB LIBRARY TO FIND SENTIMENTS AND GET THE OUTPUT """


i=0
countp=countn=countnt=0
with open('tweet.csv', 'r') as csvfile:
    rows = csv.reader(csvfile)
    for k in rows:
        sentence=re.sub(r'https?:\/\/.*[\r\n]*', '', str(k))
        blob = TextBlob(sentence)
        polar[i]=blob.sentiment.polarity
         
        if(blob.sentiment.polarity>0):
            expression='Positive';        
                
            countp+=1
        elif(blob.sentiment.polarity<0) :
            expression='Negative';
            countn +=1
        else:
            expression='Neutral';
            countnt +=1
        print(expression)    
        result[i]=expression
        i=i+1
                
            # -*- coding: utf-8 -*-
print("Positive tweets: %s"%countp)
print("Negative tweets: %s"%countn)
if(countn>=2*countp):
    print("Negative Response") 
if(countp>=2*countn):
    print("Positive Response")
    
        
df = pd.DataFrame({"Tweet":twt,"Polarity" : polar, "Sentiment" :result })
df.to_csv("sentiment.csv", index=False)        
    

with open('sentiment.csv', 'r', encoding = 'utf8') as sencsvfile:
        # Pandas to read the “Sentiment” column,
        df_sen = pd.read_csv(sencsvfile)
        sent_tweet = df_sen["Sentiment"]

#use Counter to count how many times each sentiment appears and save each as a variable
        #counter_var = Counter(sent_tweet)
Positive = countp
Negative = countn
Neutral = countnt        

## declare the variables for the pie chart, using the Counter variables for “sizes”
labels = 'Positive', 'Negative', 'Neutral'
sizes = [Positive, Negative, Neutral]
colors = ['green', 'red', 'yellow']
text = query

## use matplotlib to plot the chart
plt.pie(sizes, labels = labels, colors = colors, shadow = True, startangle = 90)
plt.title("Sentiment of 100 Tweets about "+ text)
plt.show()

    