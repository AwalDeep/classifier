# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 13:37:36 2018

@author: Awal


""""IMPORTING LIBRARIES AND HEADER FILES """


import tweepy
from tweepy import OAuthHandler
import numpy
from textblob import TextBlob
import csv
import re

""""AUTHENTICATION OF TWITTER API """

consumer_key = 'PwP7TRcyZfl4SnqEBVJSMKa6w'
consumer_secret = '3B6NnACsu22xf78BnJNVssOittaN8c0XNbVZMfyppgq9FbStV0'
access_token = '622721291-lAeWJ46G9T8sVNoCRjngZFkzAABLnnkYV6UktVmq'
access_secret = 'b42UAgFQ503Wqe8CdO7pX6jb39nkx0hOdgXeoCbJp0tF3'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)


""""GETTING INPUT FROM USER AND FETCHING TWEETS ACCORDINGLY"""


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
    
""""PROCESSING TWEETS AND STORING IT IN A CSV FILE """


for status in results:
    #print(status)
    a=((status.full_text).encode("utf-8"))
    twt.append(a)    
    
data=open('tweet.csv','w')
out= csv.writer(data) 
out.writerow(twt)      
data.close()
polar=numpy.empty(100,dtype=float)


""""USING TEXTBLOB LIBRARY TO FIND SENTIMENTS AND PRINT THE OUTPUT """


i=0
countp=countn=0
with open('tweet.csv', 'r') as csvfile:
    rows = csv.reader(csvfile)

    for row in rows:
        for k in row:
            sentence = k
            sentence = re.sub(r'https?:\/\/.*[\r\n]*', '', sentence)
            blob = TextBlob(sentence)
            polar[i]=blob.sentiment.polarity
            i=i+1 
            if(blob.sentiment.polarity>0):
                    print("Happy :)")
                    countp+=1
            else:
                print("Sad :(")
                countn +=1
                
            # -*- coding: utf-8 -*-
print("Positive tweets: %s"%countp)
print("Negative tweets: %s"%countn)
if(countn>=2*countp):
    print("Negative Response") 
if(countp>=2*countn):
    print("Positive Response")