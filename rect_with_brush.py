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
		painter = QtGui.QPainter(self.label.pixmap())
		pen = QtGui.QPen()
		pen.setWidth(3)
		pen.setColor(QtGui.QColor('#EB5160'))
		painter.setPen(pen)

		brush = QtGui.QBrush()
		brush.setColor(QtGui.QColor('#FFD141'))
		brush.setStyle(Qt.Dense1Pattern)
		painter.setBrush(brush)

		painter.drawRect(50, 50, 100, 100)
		painter.drawRect(60, 60, 150, 100)

		pen.setColor(QtGui.QColor('green'))
		painter.setPen(pen)
		painter.drawRects(
			QtCore.QRect(70, 70, 100, 150),
			QtCore.QRect(80, 80, 150, 100))


		painter.end()


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()