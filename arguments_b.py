from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

import sys

class Window(QWidget):
	def __init__(self):
		super().__init__()

		layout = QVBoxLayout()

		# not to include the py. file
		if len(sys.argv) > 0:
			file_to_open = sys.argv[-1]
			l = QLabel(file_to_open)
			layout.addWidget(l)

		self.setLayout(layout)
		self.setWindowTitle('Arguments')

app = QApplication(sys.argv)
w = Window()
w.show()

app.exec_()