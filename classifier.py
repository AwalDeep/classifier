# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 13:37:36 2018

@author: Awal
"""

import tweepy
from tweepy import OAuthHandler
import numpy
from textblob import TextBlob
import csv
import re

consumer_key = 'PwP7TRcyZfl4SnqEBVJSMKa6w'
consumer_secret = '3B6NnACsu22xf78BnJNVssOittaN8c0XNbVZMfyppgq9FbStV0'
access_token = '622721291-lAeWJ46G9T8sVNoCRjngZFkzAABLnnkYV6UktVmq'
access_secret = 'b42UAgFQ503Wqe8CdO7pX6jb39nkx0hOdgXeoCbJp0tF3'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

twt=[]
rate=api.rate_limit_status()
print("** Welcome to SENTIMENT ANALYSIS by Awal **")
"""
for status in tweepy.Cursor(api.user_timeline,user_id='Awal_Malhotra',count=100,tweet_mode='extended').items():
    a=((status.full_text).encode("utf-8"))
    twt.append(a)
"""
print("Enter 1 to search by hashtag:")
query=input("Enter the hashtag you want to perform sentiment analysis on(ex:#India):")
results=tweepy.Cursor(api.search,q=query).items(100)
#print(results)

for status in results:
    #print(status)
    a=((status.text).encode("utf-8"))
    twt.append(a)    
    
data=open('tweet.csv','w')
out= csv.writer(data) 
out.writerow(twt)      
data.close()
polar=numpy.empty(100,dtype=float)

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