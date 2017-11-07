def sub_emphasis(self, match):
	return '<em>%s</em>' %match.group(1)
from handler import Handler
import re
handler = Handler()
handler.sub('emphasis')
re.sub(r'\*(.+?)\*', handler.sub('emphasis'), 'This *is* a test')