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

		# set background color
		self.graphWidget.setBackground('w')

		# set pen to have full control
		pen = pg.mkPen(color=(255,0,0), width=15, style=QtCore.Qt.DashLine)

		# Make sure to write this before plotting
		# otherwise legend can't show 
		self.graphWidget.addLegend((50,50)) # add legend
		# plot data:
		self.graphWidget.plot(hour, temperature, pen=pen, symbol='+',
			symbolSize=30, symbolBrush=('b'),
			name = 'Sensor 1') # add label

		# symbolBrush can be any color, or QBrush type

		# set title
		#self.graphWidget.setTitle('Our Title here', color='k', size='30pt')
		# can also use HTML tag syntax
		self.graphWidget.setTitle('<span style=\"color:blue; font-size:30pt\">Our Title here</span>')

		#styles = {'color': 'r', 'font-size': '30pt'}
		#self.graphWidget.setLabel('left', 'Temperature (C)', **styles)
		#self.graphWidget.setLabel('bottom', 'Hour (H)', **styles)

		self.graphWidget.setLabel('left', '<span style=\"color:red; font-size:30px\">Temperature (C)</span>')
		self.graphWidget.setLabel('bottom', '<span style=\"color:red; font-size:30px\">Hour (H)</span>')



app = QtWidgets.QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec_()