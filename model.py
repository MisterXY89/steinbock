
from datetime import datetime
from bs4 import BeautifulSoup

WEEKDAY_STRINGS = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]

class Document:
	def __init__(self, file):
		self.file = file
		self.dateString = file.split(".html")[0].split("_")[1]
		# weekday: Monday = 0, ...
		self.date = datetime.strptime(self.dateString, '%d.%m.%Y.%H.%M')
		self.visitors = 0
		self.soup = None
		self.html = ""
		self.text = ""

	def read(self):
		with open(self.file, "r") as htmlFile:
			self.html = htmlFile.read()
		return self.getHtml()

	def getHtml(self):
		if self.html == "":
			return False
		return self.html

	def getText(self):
		if self.soup == None:
			return False
		return self.soup.get_text()

	def getSoup(self, htmlDoc=""):
		if htmlDoc == "":
			if self.soup == None:
				return False
			return self.soup
		self.soup = BeautifulSoup(htmlDoc, "lxml")
		return self.soup

	def getWeekdayString(self):
		return WEEKDAY_STRINGS[self.date.weekday()]

	def getMinuteAsHour(self):
		if self.date.minute == 0:
			return self.date.minute
		return 0.5
