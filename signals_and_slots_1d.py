import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

# subclass QMainWindow to customize our application's main window
class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.button_is_checked = True # set the default value

		self.setWindowTitle('My Signal/Slot App')


		# we need to keep a reference to the button on self
		# so that we can access it in our slot
		self.button = QPushButton('Press Me!')
		self.button.setCheckable(True) # set the widget to hold on a certain state
		self.button.released.connect(self.the_button_was_released)
		self.button.setChecked(self.button_is_checked) # use default value to set the initial state of widget

		# set the central widget of the window
		self.setCentralWidget(self.button) # place this button in the QMainWindow

	def the_button_was_released(self):
		self.button_is_checked = self.button.isChecked() # return the check state of the button
		print(self.button_is_checked)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()