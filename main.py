# Alt + shift + e ===> run selection

from os import environ
import os
import random
import tweepy
import time
from ..credentials import *

twitter_consumer_key = environ['twitter_consumer_key']
twitter_consumer_secret = environ['twitter_consumer_secret']
twitter_access_token = environ['twitter_access_token']
twitter_access_token_secret = environ['twitter_access_token_secret']

tw_auth = tweepy.OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
tw_auth.set_access_token(twitter_access_token, twitter_access_token_secret)
tw_api = tweepy.API(tw_auth)

# Create API object
api = tweepy.API(tw_auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

while True:

    file_name = ""
    all_files = []
    all_files = os.listdir("pics/testes")


    for i in range(0, len(all_files)):
        file_name = random.choice(all_files)
        # Create a tweet // limite 3mb por imagem
        #api.update_with_media("pics/testes/" + file_name, "Teste " + file_name)
        print(file_name)
        #os.remove("pics/testes/" + file_name)
        all_files.remove(file_name)
        time.sleep(1)


#for i in range(1, 10):
    #open("pics/testes/"+ str(i) +".txt","w+")