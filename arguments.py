from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

import sys

class Window(QWidget):
	def __init__(self):
		super().__init__()

		layout = QVBoxLayout()

		for arg in sys.argv:
		# sys.argv is a list of strings. All arguments are strings
			l = QLabel(arg)
			layout.addWidget(l)

		self.setLayout(layout)
		self.setWindowTitle('Arguments')

app = QApplication(sys.argv)
w = Window()
w.show()

app.exec_()