#!/usr/bin/env python2

import json
import config
import tweepy

import time
import random

def nawab_twitter_authenticate():
    auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.access_token_key, config.access_token_secret)
    api = tweepy.API(auth)
    return api

def nawab_read_list():
    proto_list = open('protobuf_list.txt', 'r')
    search_term = proto_list.readlines()
    return search_term

def nawab_store_id(tweet_id):
    ### Store a tweet id in a file
    with open("last_tid_store.txt","a") as fp:
        fp.write(str(tweet_id) + str('\n'))

def nawab_get_id():
    ### Read the last retweeted id from a file
    with open("last_tid_store.txt", "r") as fp:
        for line in fp:
            return line

def nawab_curate_list(api):
    while True:
        query = nawab_read_list()
        nawab_search(api, random.choice(query))
        time.sleep(60)

def nawab_search(api, query):
   number_of_tweets = 200

   try:
       last_id = nawab_get_id()
   except FileNotFoundError as e:
       print("No tweet id found")
       last_id = None

   try:
       if len(query) > 0:
           #for line in query:
            #   print("starting new query:\t" + line)

               tweet_search = tweepy.Cursor(api.search,
                                          q=query,
                                          tweet_mode="extended",
                                          lang='en').items(number_of_tweets)

               for tweet in tweet_search:
                   user = tweet.user.screen_name
                   id = tweet.id
                   nawab_store_id(id)
                   url = 'https://twitter.com/' + user +  '/status/' + str(id)
                   print(url)
   
   except tweepy.TweepError as e:
       print(e.reason)

                      #  if not tweet.retweeted:
                      # tweet = api.user_timeline(id, count = 1)[0]
                      # print(tweet.text)


                       #tweet.retweet()
                       #print("\t Retweeted")
                       # sleep(120)
                   #except tweepy.TweepError as e:
                       #print("\t Nawab Error: Retweet was not successful," + e.reason)

def main():
   api = nawab_twitter_authenticate()
   nawab_curate_list(api)

if __name__ == "__main__":
    main()
