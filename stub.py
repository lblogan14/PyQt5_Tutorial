import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class MainWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()

		self.label = QtWidgets.QLabel()
		# create the QPixmap object we'll draw onto
		canvas = QtGui.QPixmap(400, 300)
		# fill the entire canvas with white
		canvas.fill(Qt.white)

		self.setCentralWidget(self.label)
		self.draw_something()

	def draw_something(self):
		pass

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()