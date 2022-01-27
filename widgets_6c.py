import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle('My lineEdit app')

		widget = QLineEdit()
		# allow to set max length of input str
		widget.setMaxLength(10)
		# set a default text as placeholder
		widget.setPlaceholderText('Enter you text:')

		# perform input validation using input mask
		# _ after ; is used to represent the default blank
		widget.setInputMask('000.000.000.000;?')
		# can be used to validate IPV4 addresses

		widget.returnPressed.connect(self.return_pressed)
		widget.selectionChanged.connect(self.selection_changed)
		widget.textChanged.connect(self.text_changed)
		widget.textEdited.connect(self.text_edited)

		self.setCentralWidget(widget)

	def return_pressed(self):
		print('Return pressed!')
		self.centralWidget().setText('BOOOOOM!!!')

	def selection_changed(self):
		print('Selection changed')
		print(self.centralWidget().selectedText())

	def text_changed(self, s):
		print('Text changed...')
		print(s)

	def text_edited(self, s):
		print('Text edited...')
		print(s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()