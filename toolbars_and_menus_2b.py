import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QToolBar, QAction)

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

		# instance accept signal from QAction
		# must also pass in any QObject to act as the parent for the action
		# here is self as a reference to main window.
		button_action = QAction('Your button', self)
		# text displayed on the status bar if we have one
		button_action.setStatusTip('This is your button')
		#
		button_action.setCheckable(True)

		# trigger signal to custom function
		button_action.triggered.connect(self.onMyToolBarButtonClick)
		button_action.triggered.connect(self.onMyToolBarButtonCheck)
		toolbar.addAction(button_action)

	def onMyToolBarButtonClick(self, s):
		print('click', s)

	def onMyToolBarButtonCheck(self, check):
		print('check', check)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()