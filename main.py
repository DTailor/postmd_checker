import urllib2
import os

from bs4 import BeautifulSoup
from prettytable import PrettyTable


CWD = os.getcwd()
QUERY_STRING = "http://www.posta.md:8081/IPSWeb_item_events.asp?itemid=%s&Submit=Accept"

class Yodler(object):
	"""
	Class responsible for adding/deleting/reading
	tracking codes from tracking_codes file
	"""
	def __init__(self):
		super(Yodler, self).__init__()
		self.file_dir = os.path.join(CWD, 'tracking_codes')
		if not os.path.exists(self.file_dir):
			open(self.file_dir, 'w').close()

	def get_codes(self):
		codes = [line.strip() for line in open(self.file_dir)]
		return codes

	def remove_code(self, code):
		pass

	def add_code(self, code):
		pass


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

	def get_soup(self):
		page = urllib2.urlopen(self.query_string)
		data = page.read()
		page.close()
		self.soup = BeautifulSoup(data)

	def get_info(self):
		self.table = PrettyTable(["Data si ora locala", "Tara", "Localitatea", "Evenimentul", "Informatie aditionala"])
		self.get_soup()
		rows = self.soup.find('tbody').find_all('tr')

		for row in rows[3:]:
			cells = row.find_all("td")
			self.date_time = cells[0].get_text()
			self.country = cells[1].get_text()
			self.city = cells[2].get_text()
			self.event = cells[3].get_text()
			self.additional_info = cells[4].get_text()
			self.table.add_row([self.date_time, self.country, self.city, self.event, self.additional_info])
		print self.table

	def print_data(self):
		pass

		
if __name__ == '__main__':
	codes = Yodler().get_codes()

	for code in codes:
		PostaParser(code).get_info()