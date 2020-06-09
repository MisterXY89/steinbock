
import re
from bs4 import BeautifulSoup

class Document:
	def __init__(self, file):
		self.file = file
		self.visitors = 0
		self.date = re.sub("\s+", '', file.split(".html")[0].split("_")[1]);
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
