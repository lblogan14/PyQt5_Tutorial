import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QComboBox, QMainWindow

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle('My comboBox app')

		widget = QComboBox()
		widget.addItems(['One', 'Two', 'Three'])

		widget.currentIndexChanged.connect(self.index_changed)
		widget.currentTextChanged.connect(self.text_changed)

		# also editable, allowing users to enter values
		widget.setEditable(True)
		# need a insert policy to determine how to handle inserted value
		widget.setInsertPolicy(QComboBox.InsertAlphabetically)
		# can also limit the number of items allowed in the box
		widget.setMaxCount(5)

		self.setCentralWidget(widget)

	def index_changed(self, i): # i is an int
		print(i)

	def text_changed(self, s): # s is a str
		print(s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()