import socket
import sys

class IRC:
 
    irc = socket.socket()
    
    def __init__(self):  
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def command(self, cmd):
        self.irc.send(cmd)

    def JOIN(self, channel):
        cmd = ("JOIN %s\r\n" % channel).encode()
        self.command(cmd)

    def NICK(self, nick):
        cmd = ("NICK %s\r\n" % nick).encode()
        self.command(cmd)

    def USER(self, user, host, server, real_name):
        cmd = ("USER %s %s %s :%s\r\n" % (user, host, server, real_name)).encode()
        self.command(cmd)

    def PRIVMSG(self, target, msg):
        cmd = ("PRIVMSG %s :%s\r\n" % (target, msg)).encode()
        self.command(cmd)
        
    def send(self, chan, msg):
        self.irc.PRIVMSG(msg)
 
    def connect(self, server, channel, nick, user, real_name, host):
        print ("Connecting to:" +server)
        self.irc.connect((server, 6667))                               
        self.USER(user, host, server, real_name)
        self.NICK(nick)
        self.JOIN(channel)

    def get_text(self):
        text = self.irc.recv(2040)  #receive the text

        # Keep from 'pinging out' -- stay connected
        if text.startswith(('PING').encode()) != -1:
            self.irc.send(('PONG ' + ':arch-plex\r\n').encode())

        return text

    
