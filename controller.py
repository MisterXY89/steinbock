
import re
import glob
import requests
from model import Document
from bs4 import BeautifulSoup

class Parser:
	def __init__(self):
		self.fileDir = "files/"
		self.files = self.collectFileNames()

	def parseVisitors(self, soup):
		visitors = int(soup.find_all("div", class_="actcounter")[0]["data-value"])
		free = 70 - visitors
		return visitors, free

	def collectFileNames(self):
		""" scan files/ dir for all .html files and return them as list """
		self.fileDir
		return glob.glob(f'{self.fileDir}*.html')

	def parse(self):
		for file in self.files:
			doc = Document(file)
			doc.visitors, doc.free = self.parseVisitors(doc.getSoup(doc.read()))


parser = Parser()
parser.parse()
