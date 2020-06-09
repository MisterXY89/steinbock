
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
			doc.visitors, doc.free = self._parseVisitors(doc.getSoup(doc.read()))
			docList.append(doc)
		return docList


class Controller:
	def __init__(self):
		self.parser = Parser()
		self.docs = self.parser.parse()
		self.visualizer = Visualizer()

	def _buildDataFrameStandardVis(self, docList):
		dfList = []
		for doc in docList:
			dfList.append(
		        {
					'weekday': doc.getWeekdayString(),
		            'hour': doc.date.hour+doc.getMinuteAsHour(),
		            'visitors': doc.visitors,
		            'free':  doc.free
		        }
		    )

		return pd.DataFrame(dfList)

	def _buildDataFrameHeatmap(self, docList):
		dfList = []
		for doc in docList:
			dfList.append(
		        {
					'weekday': doc.date.weekday(),
		            'hour': doc.date.hour+doc.getMinuteAsHour(),
		            'visitors': doc.visitors
		            # 'free':  doc.free
		        }
		    )

		df = pd.DataFrame(dfList)
		heatmapData = pd.pivot_table(df, values='visitors',
                     index=['hour'],
                     columns='weekday')
		return heatmapData

	def vis(self):
		# self.visualizer.vis(self._buildDataFrameStandardVis(self.docs), x="hour", y="visitors", type="reg")
		self.visualizer.heatmap(self._buildDataFrameHeatmap(self.docs))


cont = Controller()
cont.vis()
