import sys

from PyQt5.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton, 
							QVBoxLayout, QWidget)

class AnotherWindow(QWidget):
	'''This "window" is a QWidget. If it has no parent,
	it will appear as a free-floating window.
	'''
	def __init__(self):
		super().__init__()

		layout = QVBoxLayout()
		self.label = QLabel('AnotherWindow')
		layout.addWidget(self.label)
		self.setLayout(layout)


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.button = QPushButton('Push for Window')
		self.button.clicked.connect(self.show_new_window)
		self.setCentralWidget(self.button)

	def show_new_window(self, checked):
		'''To keep this window from begin destroyed
		we need to keep a reference to the window
		on the main window self object:
		'''
		self.w = AnotherWindow()
		self.w.show()
		# If we click the button again, this window will be recreated again!
		# This new window will replace the old in the self.w variable
		# The prev window will be destroyed

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()	