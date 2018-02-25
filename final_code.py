
# coding: utf-8

# In[2]:


from tweepy import Stream 
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


consumer_key = 'nx7iu8MbuTR4QNsYfnE1jnNfh'
consumer_secret = 'pyN4ml1TZhBbNOZ6YEJyJw7lnQ3Qmi3HSSyfCabB65d8Dby12u'

access_token = '388861409-2cEyaRpUFNp5lP5WZuaGdPHRwYxQlHRXYnB051ZL'
access_token_secret = '0ykXaQ8L66wFOgnU2YqukRgfshEF0sqnNgAuBLiyefQTl'

class listener(StreamListener):
    def on_data(self,data):
        print(data)
         
    def on_error(self,status):
        print(status)
auth = OAuthHandler(consumer_key , consumer_secret)
auth.set_access_token(access_token,access_token_secret)

twitterStream = Stream(auth,listener())
twitterStream.filter(track=["obama"])
        

