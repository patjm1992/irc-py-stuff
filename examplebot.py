from bot import *
import time

srv = "Change this"
nick = "Change this"
channel = "Change this"
host = "Change this"

''' Instantiate a bot object '''
bot = Bot(srv, channel, nick, host)

''' These methods are self explanatory! '''
bot.say("Hola")
bot.change_topic("I am still a bot.")
bot.rename("Flavio")

''' To interact with the server you must sit inside a loop and call 
    listen_to_server() continuously. All the text from the server will
    be stored in 'text.' '''
while True:
    text = bot.listen_to_server()

    print (text) # See what the server is returning 

    ''' get.msgs() parses server text specifically for messages '''
    if 'Hi' in bot.get_msgs(text):
        time.sleep(1)
        bot.say("Hello.")

    elif 'pls go' in bot.get_msgs(text):
        time.sleep(1)
        bot.say("OK...")
        time.sleep(1)
        bot.die()
