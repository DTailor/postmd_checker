import urllib2

QUERY_STRING = "http://www.posta.md:8081/IPSWeb_item_events.asp?itemid=%s&Submit=Accept"


class PostaParser(object):
	"""
	Tracking number parser to posta.md in
	order to get the html and sanitize it 
	for a human readable form
	"""
	def __init__(self, track_nr):
		super(PostaParser, self).__init__()
		self.track_nr = track_nr
		self.query_string = QUERY_STRING % track_nr

	def get_html(self):
		page = urllib2.urlopen(self.query_string)
		data = page.read()
		page.close()
		return data
		

