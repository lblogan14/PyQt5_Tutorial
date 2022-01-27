import sys

from PyQt5 import QtWidgets, QtCore		# import PyQt5 before PyQtGraph
import pyqtgraph as pg
from pyqtgraph import PlotWidget, plot

class MainWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()

		self.graphWidget = pg.PlotWidget()
		self.setCentralWidget(self.graphWidget)

		hour = [1,2,3,4,5,6,7,8,9,10]
		temperature_1 = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]
		temperature_2 = [50, 35, 44, 22, 38, 32, 27, 38, 32, 44]

		# add background color to white
		self.graphWidget.setBackground('w')

		# add title
		self.graphWidget.setTitle('Our Title here', color='b', size='30pt')

		# add axis labels
		styles = {'color': '#f00', 'font-size': '20pt'}
		self.graphWidget.setLabel('left', 'Temperature (C)', **styles)
		self.graphWidget.setLabel('bottom', 'Hour (H)', **styles)

		# add legend
		self.graphWidget.addLegend()

		# add grid
		self.graphWidget.showGrid(x=True, y=True)

		# set range
		self.graphWidget.setXRange(0, 10, padding=0)
		self.graphWidget.setYRange(20, 55, padding=0)

		# plot two lines
		self.plot(hour, temperature_1, 'Sensor 1', 'r')
		self.plot(hour, temperature_2, 'Sensor 2', 'b')

	def plot(self, x, y, plotname, color):
		pen = pg.mkPen(color=color)
		self.graphWidget.plot(
			x, y, name=plotname, pen=pen, symbol='+', symbolSize=30,
			symbolBrush=(color))




app = QtWidgets.QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec_()