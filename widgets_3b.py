import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QCheckBox, QMainWindow

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle('My checkbox app')

		widget = QCheckBox('This is a checkbox')

		# For tristate
		widget.setCheckState(Qt.PartiallyChecked)
		# or: widget.setTriState(True)
		widget.stateChanged.connect(self.show_state)

		self.setCentralWidget(widget)

	def show_state(self, s):
		print(s == Qt.Checked)
		print(s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()