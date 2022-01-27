import sys
from random import choice, randint

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
		colors = ['#FFD141', '#376F9F', '#0D1F2D', '#E9EBEF', '#EB5160']
		painter = QtGui.QPainter(self.label.pixmap())
		pen = QtGui.QPen()
		pen.setWidth(3)
		painter.setPen(pen)

		for n in range(10000):
			pen.setColor(QtGui.QColor(choice(colors)))
			painter.setPen(pen)
			painter.drawPoint(
				200 + randint(-100, 100),
				150 + randint(-100, 100))
		painter.end()

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()