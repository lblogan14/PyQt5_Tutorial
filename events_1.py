import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.label = QLabel('Click in this window')
		self.setCentralWidget(self.label)

	# the following function names cannot be changed
	def mouseMoveEvent(self, e):
		self.label.setText('mouseMoveEvent')

	def mousePressEvent2(self, e):
		self.label.setText('mousePressEvent2')

	def mouseReleaseEvent(self, e):
		self.label.setText('mouseReleaseEvent')

	def mouseDoubleClickEvent(self, e):
		self.label.setText('mouseDoubleClickEvent')

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()