
import glob
from model import Document

class Parser:
	def __init__(self):
		self.fileDir = "files/"
		self.files = self._collectFileNames()

	def _parseVisitors(self, soup):
		""" find the current count of visitors in given soup """
		visitors = int(soup.find_all("div", class_="actcounter")[0]["data-value"])
		free = 70 - visitors
		return visitors, free

	def _collectFileNames(self):
		""" scan files/ dir for all .html files and return them as list """
		self.fileDir
		return glob.glob(f'{self.fileDir}*.html')

	def parse(self):
		""" public 'main' method for this class """
		for file in self.files:
			doc = Document(file)
			doc.visitors, doc.free = self._parseVisitors(doc.getSoup(doc.read()))


parser = Parser()
parser.parse()
