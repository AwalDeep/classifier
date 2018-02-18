# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 16:58:36 2018

@author: Awal
"""

import tweepy
from tweepy import OAuthHandler
consumer_key = '############'
consumer_secret = '##################'
access_token = '########################'
access_secret = '###############################'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

twt=[]

for status in tweepy.Cursor(api.home_timeline).items(100):
    a=((status.text).encode("utf-8"))
    twt.append(a)
 