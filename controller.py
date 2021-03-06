
import sys
import glob
import pandas as pd
import seaborn as sns
from model import Document
from view import Visualizer

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
		return glob.glob(f'{self.fileDir}*.html')

	def parse(self):
		""" public 'main' method for this class """
		docList = []
		for file in self.files:
			doc = Document(file)
			# only use data from where time inside opening hours
			if (doc.date.hour+doc.getMinuteAsHour()) > 23 or doc.date.hour < 9:
				continue
			doc.visitors, doc.free = self._parseVisitors(doc.getSoup(doc.read()))
			docList.append(doc)
		return docList


class Controller:
	def __init__(self):
		self.parser = Parser()
		self.docs = self.parser.parse()
		self.visualizer = Visualizer()

	def _buildDataFrame(self, docList):
		dfList = []
		for doc in docList:
			dfList.append(
		        {
					'weekday': str(doc.date.weekday() + 1) + " - " + doc.getWeekdayString(),
		            'hour': doc.date.hour + doc.getMinuteAsHour(),
		            'visitors': doc.visitors,
		            'free':  doc.free
		        }
		    )

		return pd.DataFrame(dfList)


	def vis(self, type):
		if type == "heatmap":
			self.visualizer.heatmap(self._buildDataFrame(self.docs))
		else:
			self.visualizer.vis(self._buildDataFrame(self.docs), x="hour", y="visitors", type=type)


if __name__ == '__main__':
	cont = Controller()
	if len(sys.argv) > 1:
		file, task, type = sys.argv
		if task == "vis":
			cont.vis(type)
	else:
		print("arg structure: task type")
		cont.vis("heatmap")
