import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

# subclass QMainWindow to customize our application's main window
class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.button_is_checked = False # set the default value

		self.setWindowTitle('My Signal/Slot App')

		button = QPushButton('Press Me!')
		button.setCheckable(True) # set the widget to hold on a certain state
		button.clicked.connect(self.the_button_was_toggled)
		button.setChecked(self.button_is_checked) # use default value to set the initial state of widget

		# set the central widget of the window
		self.setCentralWidget(button) # place this button in the QMainWindow

	def the_button_was_toggled(self, anyCheckName):
		self.button_is_checked = anyCheckName # when widget state changes, update the variable to match
		print(self.button_is_checked)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()