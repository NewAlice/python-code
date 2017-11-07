from urllib2 import urlopen
import re
p = re.compile('<h3><a .*?><a .*? href="(.*?)">(.*?)</a>')
text = urlopen('https://www.python.org/jobs/').read()
for url,name in p.findall(text):
	print '%s (%s)' %(name, url)