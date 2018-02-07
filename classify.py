# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 23:11:15 2018

@author: Awal
"""
import fetch 
import numpy
from textblob import TextBlob
import csv
data=open('tweet.csv','w')
out= csv.writer(data) 
out.writerow(fetch.twt)         
data.close()
polar=numpy.empty(100,dtype=float)

i=0
countp=countn=0
with open('tweet.csv', 'r') as csvfile:
    rows = csv.reader(csvfile)

    for row in rows:
        for k in row:
            sentence = k
            blob = TextBlob(sentence)
            polar[i]=blob.sentiment.polarity
            i=i+1 
            if(blob.sentiment.polarity>0):
                    print("Positive")
                    countp+=1
            else:
                print("Negative")
                countn +=1
                
            # -*- coding: utf-8 -*-

