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

    def TOPIC(self, channel, topic):
        cmd = ("TOPIC %s :%s\r\n" % (channel, topic)).encode()
        self.command(cmd)

    def QUIT(self):
        """ TO-DO """
        
    def connect(self, server, channel, nick, user, real_name, host):
        print ("Connecting to: %s..." % server)
        self.host = host
        self.irc.connect((server, 6667))                               
        self.USER(user, host, server, real_name)
        self.NICK(nick)
        self.JOIN(channel)

    def get_text(self):
        data = self.irc.recv(2040)

        if data.startswith(('PING').encode()) != -1:
#            self.irc.send(('PONG ' + ':arch-plex\r\n' % ).encode())
            self.irc.send(('PONG :%s\r\n' % self.host).encode())

        text = data.decode()
            
        return text

    
