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
		pen.setWidth(1)
		pen.setColor(QtGui.QColor('green'))
		painter.setPen(pen)

		font = QtGui.QFont()
		font.setFamily('Times')
		font.setBold(True)
		font.setPointSize(40)
		painter.setFont(font)

		painter.drawText(100, 100, 'Hello World!')

		pen.setColor(QtGui.QColor('yellow'))
		painter.setPen(pen)
		# arguments: x_pos, y_pos, width, height, of boudning box; alignment; text
		# text outside this box is clipped
		painter.drawText(100, 100, 100, 100, Qt.AlignHCenter, 'Hello world!')


		painter.end()


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()