import urllib2

QUERY_STRING = "http://www.posta.md:8081/IPSWeb_item_events.asp?itemid=%s&Submit=Accept"


def query_string(code):
	return QUERY_STRING % code

def read_link(link):
	page = urllib2.urlopen(link)
	data = page.read()
	page.close()
	return data
