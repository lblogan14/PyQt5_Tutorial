import sys

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QLabel, QToolBar, QStatusBar, QCheckBox
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle('My menus app')

		label = QLabel('Hello!')
		label.setAlignment(Qt.AlignCenter)

		# set central widget in mainwindow
		self.setCentralWidget(label)


		# set toolbar in mainwindow
		toolbar = QToolBar('My main toolbar')
		# set the icon size with QSize object
		toolbar.setIconSize(QSize(25,25))
		self.addToolBar(toolbar)

		button_action = QAction(QIcon('cat.jpg'), '&Your button', self)
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

		# this shows both the icon and text in toolbar
		toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
		# set status bar in mainwindow
		self.setStatusBar(QStatusBar(self))

		# Set up the menu in mainwindow
		menu = self.menuBar()
		# The & for quick key when pressing Alt
		file_menu = menu.addMenu('&File')
		# we can reuse the existing QAction to add the same function to menu
		file_menu.addAction(button_action)
		file_menu.addSeparator()

		# add sub menu
		file_submenu = file_menu.addMenu('SubMenu')
		file_submenu.addAction(button_action2)

	def onMyToolBarButtonClick(self, s):
		print('click', s)

app = QApplication(sys.argv)
# set the style here
#app.setStyle('Fusion')
app.setStyle('Windows')

window = MainWindow()
window.show()

app.exec_()