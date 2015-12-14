from irc import *

class Bot:

    irc = IRC()
    
    def __init__(self, srv, chan, nick, host):
        self.irc.connect(srv, chan, nick, "bot", "bot", host)
        self.srv = srv
        self.chan = chan
        self.nick = nick
        self.host = host

    def listen_to_server(self):
        text = self.irc.get_text()
        return text
        
    def say(self, something):
        self.irc.PRIVMSG("#atildae", something)

    def get_msgs(self, text):
        msg = ""
        
        if "PRIVMSG" in text:
            line = text.split(":")
            msg = line[2]
            print ("PRIVMSG RECEIVED: %s" % msg)
        
        return msg
        
    def change_topic(self, new_topic):
        self.irc.TOPIC(self.chan, new_topic)
        
    def leave(self):
        pass
        
    def reconnect(self):
        pass
    
    def die(self):
        leave()
        sys.exit()
    
    def rename(self, new_name):
        self.irc.NICK(new_name)

    
