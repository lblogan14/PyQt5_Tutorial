import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.label = QLabel('Click in this window')
		self.setMouseTracking(True)
		self.setCentralWidget(self.label)

	# the following function names cannot be changed
	# it will not work if we modify it
	# moveEvent only registered when we pressed the button and move.
	# we can change this by calling:
		

	def mouseMoveEvent(self, e):
		self.label.setText('mouseMoveEvent')

	def mousePressEvent(self, e):
		self.label.setText('mousePressEvent')

	def mouseReleaseEvent(self, e):
		self.label.setText('mouseReleaseEvent')

	def mouseDoubleClickEvent(self, e):
		self.label.setText('mouseDoubleClickEvent')

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()