import sys

from PyQt5 import QtWidgets		# import PyQt5 before PyQtGraph
import pyqtgraph as pg
from pyqtgraph import PlotWidget, plot

class MainWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()

		self.graphWidget = pg.PlotWidget()
		self.setCentralWidget(self.graphWidget)

		hour = [1,2,3,4,5,6,7,8,9,10]
		temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]

		# plot data:
		self.graphWidget.setBackground('w')
		self.graphWidget.plot(hour, temperature)

app = QtWidgets.QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec_()