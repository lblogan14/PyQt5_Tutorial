import sys

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QLabel, QToolBar, QStatusBar, QCheckBox
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle('My status bar app')

		label = QLabel('Hello!')
		label.setAlignment(Qt.AlignCenter)

		# set central widget in mainwindow
		self.setCentralWidget(label)

		# set toolbar in mainwindow
		toolbar = QToolBar('My main toolbar')
		# set the icon size with QSize object
		toolbar.setIconSize(QSize(25,25))
		self.addToolBar(toolbar)

		button_action = QAction(QIcon('cat.jpg'), 'Your button', self)
		button_action.setStatusTip('This is your button')
		button_action.triggered.connect(self.onMyToolBarButtonClick)
		# turn the QAction toggleable
		button_action.setCheckable(True)
		toolbar.addAction(button_action)

		# add a vertical line as separator
		toolbar.addSeparator()

		button_action2 = QAction(QIcon('cat.jpg'), 'Your button2', self)
		button_action2.setStatusTip('This is your second button')
		button_action2.triggered.connect(self.onMyToolBarButtonClick)
		button_action2.setCheckable(True)
		toolbar.addAction(button_action2)

		toolbar.addSeparator()

		toolbar.addWidget(QLabel('Hello world'))
		toolbar.addWidget(QCheckBox())

		toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
		# set status bar in mainwindow
		self.setStatusBar(QStatusBar(self))

	def onMyToolBarButtonClick(self, s):
		print('click', s)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()