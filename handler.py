def sub_emphasis(self, match):
	return '<em>%s</em>' %match.group(1)
class Handler:
	def callback(self, prefix, name, *args):
		method = getattr(self, prefix+name, None)
		if callable(method): return method(*args)
	def start(self, name):
		self.callback('start_', name)
	def end(self, name):
		self.callback('end_', name)
	def sub(self, name):
		def substitution(match):
			result = self.callback('sub_',name, match)
			if result is None: match.group(0)
			return result
		return substitution


from handler import Handler
import re
handler = Handler()
handler.sub('emphasis')
re.sub(r'\*(.+?)\*', handler.sub('emphasis'), 'This *is* a test')