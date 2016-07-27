# coding: utf-8
import re
import irclib
import ircbot
import math
import base64

print "Bot started"
def rot13(s):
    result = ""
    # Loop over characters.
    for v in s:
        # Convert to number with ord.
        c = ord(v)
        # Shift number back or forward.
        if c >= ord('a') and c <= ord('z'):
            if c > ord('m'):
                c -= 13
            else:
                c += 13
        elif c >= ord('A') and c <= ord('Z'):
            if c > ord('M'):
                c -= 13
            else:
                c += 13
        # Append to result.
        result += chr(c)
    # Return transformation.
    return result

class BotGamesurge(ircbot.SingleServerIRCBot):
    def __init__(self):
	ircbot.SingleServerIRCBot.__init__(self, [('irc.root-me.org', 6667)],'Polo_leBot', 'Chaîne encodée')
    def on_welcome(self, serv, ev):
        self.pm = serv.privmsg('Candy', '!ep3')
        print 'Message envoyé !ep3'

    def on_privmsg(self, serv, ev):
    	print 'Message reçu : ' + ev.arguments()[0]
    	result = rot13(ev.arguments()[0])
        self.pm = serv.privmsg('Candy', '!ep3 -rep '+str(result))
    	print 'Message envoyé : '+str(result)


BotGamesurge().start()
