import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

# subclass QMainWindow to customize our application's main window
class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.button_is_checked = True # set the default value

		self.setWindowTitle('My Signal/Slot App')

		# need to access the button in our the_button_was_clicked method,
		# so we need to keep a refernce to it on self.
		self.button = QPushButton('Press Me!')
		self.button.clicked.connect(self.the_button_was_clicked)

		# set the central widget of the window
		self.setCentralWidget(self.button) # place this button in the QMainWindow

	def the_button_was_clicked(self):
		self.button.setText('Just clicked the button.')
		self.button.setEnabled(False)

		# also change the window title
		self.setWindowTitle('One shot app')

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()