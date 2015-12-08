from irc import *

class Bot:

    def __init__(self, name):
        irc = IRC()
        irc.connect("74.75.50.221", "#atildae", name, "bot", "bot", "arch-plex")

    def listen_to_server(self):
        text = irc.get_text()
        print text
        
    def say(self, something):
        irc.PRIVMSG("#atildae", something)

    def get_msgs(self):
        """ Parse text for private messages from users in the channel. """
        """ TO-DO """
        return msg
        
    def change_topic(self, new_topic):
        irc.TOPIC(new_topic)
        
    def leave(self):
        
    def reconnect(self):
        
    def die(self):
        leave()
        sys.exit()
    
    def rename(self, new_name):
        irc.NICK(new_name)

    
