import tweepy

api_key = " "
api_key_secret = " "
access_token = " "
access_token_secret = " "
bearer_token = " "

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# api.create_friendship(screen_name = " ")
# api.get_direct_message()

user = api.get_user(screen_name="enter_twitter_username")
ID = user.id_str
print("The ID of the user is : " + ID)
for i in range(5):
    text = "How r u bro?"
    api.send_direct_message(ID, text)

# api.update_profile(description="I like Python")

# api.update_status("Test tweet from Tweepy Python")
# api.update_status(status="Namaste India")

# public_tweets = api.home_timeline()
# print(public_tweets)


# authentication twitter v2

# client = tweepy.Client(bearer_token,api_key,api_key_secret,access_token,access_token_secret)
# auth = tweepy.OAuth1UserHandler(bearer_token,api_key,api_key_secret,access_token,access_token_secret)
# api = tweepy.API(auth)
# client.create_tweet(text="hello")
# client.create_tweet(text = "This is our first tweets")
# client.delete_tweet(id=1560256831091802112)
# client.follow_user(target_user_id="niteshxp")
# client.like(1560253570095935490)
# for tweet in api.home_timeline():
#     print(tweet.text)
# person = client.get_user(username="MLBot123").data.id
# for tweet in client.get_users_tweets(person).data:
#     print(tweet.text)
