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

		self.label.setPixmap(canvas)

		self.setCentralWidget(self.label)
		self.draw_something()

	def draw_something(self):
		painter = QtGui.QPainter(self.label.pixmap())
		# draw a line from (10, 10) to (300, 200)
		# (x=0,y=0) is in the top left
		painter.drawPoint(200, 150)
		painter.end()

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()