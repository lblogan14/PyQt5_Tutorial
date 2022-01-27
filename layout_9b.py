import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
							QTabWidget, QPushButton)

# import the Color class we just created
from layout_colorwidget import Color

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle('My tab app')

		tabs = QTabWidget()
		# set the position of tabs using the 
		# cardinal directions
		tabs.setTabPosition(QTabWidget.West)
		# set the tabs are moveable
		tabs.setMovable(True)
		# turn on document mode for slimline tabs on macos
		tabs.setDocumentMode(True)

		for n, color in enumerate(['red', 'green', 'blue', 'yellow']):
			tabs.addTab(Color(color), color)

		# QTabWidget is already a widget, can be set directly
		self.setCentralWidget(tabs)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()

# this will give us the border around the red widget,
# this is the layout spacing