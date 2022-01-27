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
		pen.setColor(QtGui.QColor(204, 0, 0)) #r,g,b
		painter.setPen(pen)

		# arguments: x, y, width, height
		painter.drawEllipse(10, 10, 100, 100)
		painter.drawEllipse(10, 10, 150, 200)
		painter.drawEllipse(10, 10, 200, 300)

		# we can also use QRect 
		pen.setColor(QtGui.QColor('blue'))
		painter.setPen(pen)
		painter.drawEllipse(QtCore.QRect(50, 50, 100, 100))

		# we can also take the center of ellipse as 1st parameter,
		# and then x, y radius.
		pen.setColor(QtGui.QColor('purple'))
		painter.setPen(pen)
		painter.drawEllipse(QtCore.QPoint(100,100), 15, 20)
		painter.drawEllipse(QtCore.QPoint(300,150), 50, 50)

		painter.end()


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()