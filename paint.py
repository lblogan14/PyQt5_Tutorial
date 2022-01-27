import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class Canvas(QtWidgets.QLabel):
	def __init__(self):
		super().__init__()

		pixmap = QtGui.QPixmap(600, 300)
		pixmap.fill(Qt.white)
		self.setPixmap(pixmap)

		self.last_x, self.last_y = None, None
		self.pen_color = QtGui.QColor('#000000')

	def set_pen_color(self, c):
		self.pen_color = QtGui.QColor(c)

	def mouseMoveEvent(self, e):
		if self.last_x is None: # first event
			self.last_x = e.x()
			self.last_y = e.y()
			return # ignore the first time

		painter = QtGui.QPainter(self.pixmap())
		p = painter.pen()
		p.setWidth(4)
		p.setColor(self.pen_color)
		painter.setPen(p)
		painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
		painter.end()
		self.update()

		# update the origin for next time
		self.last_x = e.x()
		self.last_y = e.y()

	def mouseReleaseEvent(self, e):
		self.last_x = None
		self.last_y = None

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()