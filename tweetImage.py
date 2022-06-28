# Copyright (c) 2022 Michio Inoue.
#  py.tweetImage.tweetWithImage('過去 7 日間のツイートの wordcloud をただツイートする自動化テスト','wordcloud_weekly.png')
def tweetWithImage(status, path2image):

    import tweepy
    from os import getenv
    
    consumerkey = getenv('CONSUMERKEY');
    consumersecret = getenv('CONSUMERSECRET');
    accesstoken = getenv('ACCESSTOKEN');
    accesstokensecret = getenv('ACCESSTOKENSECRET');
    
    auth = tweepy.OAuthHandler(consumerkey, consumersecret)
    auth.set_access_token(accesstoken, accesstokensecret)
    
    api = tweepy.API(auth)
    
    #tweet
    # Deprecated since version 3.7.0: Use API.media_upload() instead.
    # Changed in version 4.0: Renamed from API.update_with_media
    # https://docs.tweepy.org/en/stable/api.html
    api.update_status_with_media(status = status, filename = path2image)