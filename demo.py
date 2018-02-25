from flask import Flask, render_template
import tweepy
from textblob import TextBlob

consumer_key = 'nx7iu8MbuTR4QNsYfnE1jnNfh'
consumer_secret = 'pyN4ml1TZhBbNOZ6YEJyJw7lnQ3Qmi3HSSyfCabB65d8Dby12u'

access_token = '388861409-2cEyaRpUFNp5lP5WZuaGdPHRwYxQlHRXYnB051ZL'
access_token_secret = '0ykXaQ8L66wFOgnU2YqukRgfshEF0sqnNgAuBLiyefQTl'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

app = Flask(__name__)
api = tweepy.API(auth)


@app.route('/search/<keyword>')
def search(keyword):
    public_tweets = api.search('keyword')
    out  = ""
    for tweet in public_tweets:
        #analysis = TextBlob(tweet.text)
        out  += tweet.text
    return out



