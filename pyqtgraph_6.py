import sys
import os
from random import randint

from PyQt5 import QtWidgets, QtCore		# import PyQt5 before PyQtGraph
import pyqtgraph as pg
from pyqtgraph import PlotWidget, plot

class MainWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()

		self.graphWidget = pg.PlotWidget()
		self.setCentralWidget(self.graphWidget)

		self.x = list(range(100)) # 100 time points
		self.y = [randint(0, 100) for _ in range(100)] # 100 data points

		# add background color to white
		self.graphWidget.setBackground('w')

		pen = pg.mkPen(color=(255,0,0))

		# take a reference to the line we plotted, storing it as self.data_line
		self.data_line = self.graphWidget.plot(self.x, self.y, pen=pen)		

		self.timer = QtCore.QTimer()
		self.timer.setInterval(50)
		self.timer.timeout.connect(self.update_plot_data)
		self.timer.start()




	def update_plot_data(self):
		self.x = self.x[1:] # remove the first x element
		self.x.append(self.x[-1] + 1) # add a new value 1 higher than the last

		self.y = self.y[1:] # remove the first y element
		self.y.append(randint(0, 100)) # add a new random value

		self.data_line.setData(self.x, self.y) # udpate the data




app = QtWidgets.QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec_()