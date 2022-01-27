import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QToolBar)

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle('My toolbar app')

		label = QLabel('Hello!')
		label.setAlignment(Qt.AlignCenter)

		# this is the central widget in mainwindow
		self.setCentralWidget(label)

		# set up the toolbar in mainwindow
		toolbar = QToolBar('my main toolbar')
		self.addToolBar(toolbar) # required for mainwindow

	def onMyToolBarButtonClick(self, s):
		print('click', s)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()