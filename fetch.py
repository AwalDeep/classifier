# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 16:58:36 2018

@author: Awal
"""

import tweepy
from tweepy import OAuthHandler
consumer_key = 'PwP7TRcyZfl4SnqEBVJSMKa6w'
consumer_secret = '3B6NnACsu22xf78BnJNVssOittaN8c0XNbVZMfyppgq9FbStV0'
access_token = '622721291-lAeWJ46G9T8sVNoCRjngZFkzAABLnnkYV6UktVmq'
access_secret = 'b42UAgFQ503Wqe8CdO7pX6jb39nkx0hOdgXeoCbJp0tF3'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

twt=[]

for status in tweepy.Cursor(api.home_timeline).items(100):
    a=((status.text).encode("utf-8"))
    twt.append(a)
 