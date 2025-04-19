#INSTAGRAM AUTOMATION

from instabot import Bot
bot=Bot()
bot.login(username="Username",password="Password")
bot.follow("flowers_name")  #IF THIS ACCOUNT IS FOLLOW THEN IT SHOW TRUE OTHERWISE FALSE
bot.unfollow("user_name")   #FOR UNFOLLOW A ID
bot.upload_photo("photolink",caption="caption") #for uploading pictures
bot.send_message("Message",["Idname","password"])

