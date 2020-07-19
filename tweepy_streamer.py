from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import twitter_credentials

class TwitterStreamer():
        """
        Streams and processes live tweets.
        """
        # handles twitter authentification and connection to Tweepy API
        def stream_tweets(self, fetched_tweet_filename, hash_tag_list):
            #create StreamListener child object (see class below)
            listener = StdOutListener(fetched_tweet_filename)
            #create authorization var by accessing twitter_credentials.py
            auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
            auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)

            #create twitter stream
            stream = Stream(auth, listener)
            #filter tweet based on keywords in list
            stream.filter(track = hash_tag_list)


#create derived StreamListener Object
class StdOutListener(StreamListener):
    """
    Listener class that prints tweets to stdout
    """
    def __init__(self, fetched_tweet_filename):
        self.fetched_tweet_filename = fetched_tweet_filename
    
    #override on_data and on_error classes
    def on_data(self, data):
        try:
            print(data) #can delete print statement if you just want to write data
            with open(self.fetched_tweet_filename, 'a') as tf:
                tf.write(data)
                return True
        except BaseException as e:
            print("Error on data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)

# main function
if __name__ == "__main__":
    hash_tag_list = []
    fetched_tweet_filename = "tweets.json"

    # create TwitterStreamer object
    twitter_streamer = TwitterStreamer()
    # call stream_tweets method to actually stream tweets
    twitter_streamer.stream_tweets(fetched_tweet_filename, hash_tag_list)
