from InternetSpeedTwitterBot import InternetSpeedTwitterBot

with open('data.txt', "r") as f:
    lines = f.readlines()

TWITTER_EMAIL = lines[0].replace('TWITTER_EMAIL = ', '').replace('\n', '').replace('"', '')
TWITTER_PASSWORD = lines[1].replace('TWITTER_PASSWORD = "', '').replace('\n', '').replace('"', '')
TWITTER_USER_NAME = lines[2].replace('TWITTER_USER_NAME = "', '').replace('"', '')
YOUR_INTERNET_PROVIDER = 'Internet Provider'
PROMISED_DOWN = 1000
PROMISED_UP = 90


bot = InternetSpeedTwitterBot(user_name=TWITTER_USER_NAME,e_mail=TWITTER_EMAIL, password=TWITTER_PASSWORD,
                              down=PROMISED_DOWN, up=PROMISED_UP, provider=YOUR_INTERNET_PROVIDER)
down_up = bot.get_internet_speed()
bot.tweet_at_provider(down_speed= down_up[0], up_speed=down_up[1])