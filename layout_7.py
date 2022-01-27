import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QStackedLayout

# import the Color class we just created
from layout_colorwidget import Color

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle('My stacked layout app')

		layout = QStackedLayout()
		# add 4 laytouts
		layout.addWidget(Color('red'))
		layout.addWidget(Color('green'))
		layout.addWidget(Color('blue'))
		layout.addWidget(Color('yellow'))
		# select the one we want to show
		layout.setCurrentIndex(2)

		widget = QWidget()
		widget.setLayout(layout)

		self.setCentralWidget(widget)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()

# this will give us the border around the red widget,
# this is the layout spacing