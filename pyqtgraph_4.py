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
		temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]

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
		self.graphWidget.setXRange(0, 10, padding=0.1)
		self.graphWidget.setYRange(20, 55, padding=0)

		pen = pg.mkPen(color=(255,0,0), width=5, style=QtCore.Qt.DashLine)
		# plot data:
		self.graphWidget.plot(hour, temperature, pen=pen, symbol='+',
			symbolSize=30, symbolBrush=('b'),
			name = 'Sensor 1') # add label



app = QtWidgets.QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec_()