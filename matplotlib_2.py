import sys

# import PyQt5 before matplotlib
from PyQt5 import QtWidgets 

import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
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

		# create the matplotlib FigureCanvas object,
		# which defines a single set of axes as self.axes
		sc = MplCanvas(self, width=5, height=5, dpi=100)
		sc.axes.plot([0,1,2,3,4], [10,1,20,3,40])

		# create toolbar, passing canvas as first parameter, parent(self, the MainWindow) as second
		toolbar = NavigationToolbar(sc, self)

		layout = QtWidgets.QVBoxLayout()
		layout.addWidget(toolbar)
		layout.addWidget(sc)

		# create a placeholder widget to hold our toolbar and canvas
		widget = QtWidgets.QWidget()
		widget.setLayout(layout)

		self.setCentralWidget(widget)

		self.show()

app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()