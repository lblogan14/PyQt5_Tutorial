import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QSpinBox, QMainWindow

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle('My spinBox app')

		# SpinBox is for integers
		widget = QSpinBox()
		widget.setMinimum(-10)
		widget.setMaximum(10)
		# or: widget.setRange(-10, 10)

		widget.setPrefix('$')
		widget.setSuffix('c')
		widget.setSingleStep(2) # jump 2 for a click
		widget.valueChanged.connect(self.value_changed)
		widget.valueChanged[str].connect(self.value_changed_str)


		self.setCentralWidget(widget)

	def value_changed(self, i):
		print(i)

	def value_changed_str(self, s):
		# this returns the entire str in the box
		print(s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()