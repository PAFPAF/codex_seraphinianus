# Alt + shift + e ===> run selection

from os import environ
import os
import random
import tweepy
import time
import datetime

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
    all_files = os.listdir("pics/pages")


    for i in range(0, len(all_files)):
        file_name = random.choice(all_files)
        #Create a tweet // limite 3mb por imagem
        api.update_with_media("pics/pages/" + file_name, "#CodexSeraphinianus")
        print(file_name)
        all_files.remove(file_name)


        sleep_until = "5:50PM"  # Sets the time to sleep until.
        sleep_until = time.strftime("%m/%d/%Y " + sleep_until,
        time.localtime())  # Adds todays date to the string sleep_until.
        now_epoch = time.time()  # Current time in seconds from the epoch time.
        alarm_epoch = time.mktime(
        time.strptime(sleep_until, "%m/%d/%Y %I:%M%p"))  # Sleep_until time in seconds from the epoch time.
        if now_epoch > alarm_epoch:  # If we are already past the alarm time today.
            alarm_epoch = alarm_epoch + 86400  # Adds a day worth of seconds to the alarm_epoch, hence setting it to next day instead.
        time.sleep(alarm_epoch - now_epoch)  # Sleeps until the next time the time is the set time, whether it's today or tomorrow.


#for i in range(1, 5):
    #open("pics/testes/"+ str(i) +".txt","w+")