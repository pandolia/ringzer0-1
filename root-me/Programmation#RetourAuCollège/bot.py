# coding: utf-8
import re
import irclib
import ircbot
import math


print "Bot started"

class BotGamesurge(ircbot.SingleServerIRCBot):
    def __init__(self):
	ircbot.SingleServerIRCBot.__init__(self, [('irc.root-me.org', 6667)],'Polo_leBot', 'Retour au collège')
    def on_welcome(self, serv, ev):
	       self.pm = serv.privmsg('Candy', '!ep1')
    def on_privmsg(self, serv, ev):
    	print 'Message reçu : ' + ev.arguments()[0]
    	matchObj = re.match('[0-9]+ \/ [0-9]+', ev.arguments()[0])
    	if matchObj:
    		numbers = ev.arguments()[0].split('/')
    		result = round(math.sqrt(float(numbers[0])) * float(numbers[1]),2)
    		self.pm = serv.privmsg('Candy', '!ep1 -rep '+str(result))
    		print 'Message envoyé : '+str(result)
    	else:
    		pass

BotGamesurge().start()
