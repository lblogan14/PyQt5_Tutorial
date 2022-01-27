import sys
import random

# import PyQt5 before matplotlib
from PyQt5 import QtWidgets, QtCore 

import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

matplotlib.use('Qt5Agg')

class MplCanvas(FigureCanvasQTAgg):
	def __init__(self, parent=None, width=5, height=4, dpi=100):
		fig = Figure(figsize=(width, height), dpi=dpi)
		self.axes = fig.add_subplot(111)
		super().__init__(fig)

class MainWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()

		self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
		self.setCentralWidget(self.canvas)

		n_data = 50
		self.xdata = list(range(n_data))
		self.ydata = [random.randint(0,10) for i in range(n_data)]
		self.update_plot()

		self.show()

		# setup a timer to trigger the redraw by calling update_plot
		self.timer = QtCore.QTimer()
		self.timer.setInterval(100)
		self.timer.timeout.connect(self.update_plot)
		self.timer.start()

	def update_plot(self):
		# drop off the first y element, append a new one
		self.ydata = self.ydata[1:] + [random.randint(0,10)]
		self.canvas.axes.cla() # clear the canvas
		self.canvas.axes.plot(self.xdata, self.ydata, 'r')

		# trigger the canvas to update the redraw
		self.canvas.draw()

app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()