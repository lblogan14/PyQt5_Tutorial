import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.label = QLabel('Click in this window')
		self.setCentralWidget(self.label)

	# the following function names cannot be changed
	# it will not work if we modify it
	def mouseMoveEvent(self, e):
		self.label.setText('mouseMoveEvent')

	def mousePressEvent(self, e):
		if e.button() == Qt.LeftButton:
			# handle the left-button press
			self.label.setText('mousePressEvent LEFT')
		elif e.button() == Qt.MiddleButton:
			# handle the middle-button press
			self.label.setText('mousePressEvent MIDDLE')
		elif e.button() == Qt.RightButton:
			# handle the right-button press
			self.label.setText('mousePressEvent RIGHT')

	def mouseReleaseEvent(self, e):
		if e.button() == Qt.LeftButton:
			self.label.setText('mouseReleaseEvent LEFT')
		elif e.button() == Qt.MiddleButton:
			self.label.setText('mouseReleaseEvent MIDDLE')
		elif e.button() == Qt.RightButton:
			self.label.setText('mouseReleaseEvent RIGHT')

	def mouseDoubleClickEvent(self, e):
		if e.button() == Qt.LeftButton:
			self.label.setText('mouseDoubleClickEvent LEFT')
		elif e.button() == Qt.MiddleButton:
			self.label.setText('mouseDoubleClickEvent MIDDLE')
		elif e.button() == Qt.RightButton:
			self.label.setText('mouseDoubleClickEvent RIGHT')

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()