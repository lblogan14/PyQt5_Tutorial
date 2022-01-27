import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from custom_canvas import Canvas
from color_button import QPaletteButton, COLORS

class MainWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()

		self.canvas = Canvas()

		w = QtWidgets.QWidget()
		l = QtWidgets.QVBoxLayout()
		w.setLayout(l)
		l.addWidget(self.canvas)

		palette = QtWidgets.QHBoxLayout()
		self.add_palette_buttons(palette)
		l.addLayout(palette)

		self.setCentralWidget(w)

	def add_palette_buttons(self, layout):
		for c in COLORS:
			b = QPaletteButton(c)
			b.pressed.connect(lambda c=c: self.canvas.set_pen_color(c))

			layout.addWidget(b)



app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()