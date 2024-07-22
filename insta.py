from instabot import Bot

# Login credentials
USERNAME = 'pytho_n12357'
PASSWORD = 'test_user12@'

# Initialize the bot
bot = Bot()

# Login to Instagram
bot.login(username=USERNAME, password=PASSWORD)

# Path to the picture you want to post
photo_path = '/root/python/photo.jpg'

# Caption for the post
caption = 'Hello '

# Post the picture
bot.upload_photo(photo_path, caption=caption)

bot.logout()
