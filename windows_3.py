import sys

from random import randint

from PyQt5.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton, 
							QVBoxLayout, QWidget)

class AnotherWindow(QWidget):
	def __init__(self):
		super().__init__()

		layout = QVBoxLayout()
		self.label = QLabel('AnotherWindow %d' % randint(0,100))
		layout.addWidget(self.label)
		self.setLayout(layout)


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		# to prevent window being recreated, need to check
		self.w = None # No external window yet.		
		self.button = QPushButton('Push for Window')
		self.button.clicked.connect(self.show_new_window)
		self.setCentralWidget(self.button)

	def show_new_window(self, checked):
		if self.w is None:
			self.w = AnotherWindow()
			self.w.show()

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()	