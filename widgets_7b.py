import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDoubleSpinBox, QMainWindow

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle('My spinBox app')

		# DoubleSpinBox is for float
		widget = QDoubleSpinBox()
		widget.setMinimum(-5)
		widget.setMaximum(5)
		# or: widget.setRange(-5, 5)

		widget.setPrefix('$')
		widget.setSuffix('c')
		widget.setSingleStep(0.1) # jump 2 for a click
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