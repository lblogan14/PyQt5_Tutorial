import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow

# import the Color class we just created
from layout_colorwidget import Color

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle('My color custom class app')

		widget = Color('red')

		self.setCentralWidget(widget)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()