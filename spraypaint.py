import sys
import random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

SPRAY_PARTICLES = 100
SPRAY_DIAMETER = 10

class Canvas(QtWidgets.QLabel):
	def __init__(self):
		super().__init__()

		pixmap = QtGui.QPixmap(600, 300)
		pixmap.fill(Qt.white)
		self.setPixmap(pixmap)

		self.pen_color = QtGui.QColor('#000000')

	def set_pen_color(self, c):
		self.pen_color = QtGui.QColor(c)

	def mouseMoveEvent(self, e):
		painter = QtGui.QPainter(self.pixmap())
		p = painter.pen()
		p.setWidth(1)
		p.setColor(self.pen_color)
		painter.setPen(p)

		for n in range(SPRAY_PARTICLES):
			xo = random.gauss(0, SPRAY_DIAMETER)
			yo = random.gauss(0, SPRAY_DIAMETER)
			painter.drawPoint(e.x() + xo, e.y() + yo)

		self.update()