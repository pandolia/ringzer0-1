# coding: utf-8
import re
import irclib
import ircbot
import math
import base64

print "Bot started"

class BotGamesurge(ircbot.SingleServerIRCBot):
    def __init__(self):
	ircbot.SingleServerIRCBot.__init__(self, [('irc.root-me.org', 6667)],'Polo_leBot', 'Chaîne encodée')
    def on_welcome(self, serv, ev):
        self.pm = serv.privmsg('Candy', '!ep2')
        print 'Message envoyé !ep2'

    def on_privmsg(self, serv, ev):
    	print 'Message reçu : ' + ev.arguments()[0]
    	result = base64.b64decode(ev.arguments()[0])
        self.pm = serv.privmsg('Candy', '!ep2 -rep '+str(result))
    	print 'Message envoyé : '+str(result)


BotGamesurge().start()
