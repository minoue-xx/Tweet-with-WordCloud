# Copyright (c) 2022 Michio Inoue.
#  py.tweetImage.tweetWithImage('過去 7 日間のツイートの wordcloud をただツイートする自動化テスト','wordcloud_weekly.png')
def tweetWithImage(status, path2image):

    import tweepy
    from os import getenv
    
    consumer_key = getenv('consumer_key')
    consumer_secret = getenv('consumer_secret')
    access_token = getenv('access_token')
    access_token_secret = getenv('access_token_secret') 
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    api = tweepy.API(auth)
    
    #tweet
    # Deprecated since version 3.7.0: Use API.media_upload() instead.
    # Changed in version 4.0: Renamed from API.update_with_media
    # https://docs.tweepy.org/en/stable/api.html
    api.update_status_with_media(status = status, filename = path2image)