import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

# subclass QMainWindow to customize our application's main window
class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle('My Signal/Slot App')

		button = QPushButton('Press Me!')
		button.setCheckable(True)
		# first slot
		button.clicked.connect(self.the_button_was_clicked)
		# second slot
		button.clicked.connect(self.the_button_was_toggled)

		# set the central widget of the window
		self.setCentralWidget(button) # place this button in the QMainWindow

	def the_button_was_clicked(self):
		print('I just clicked the button!')
	def the_button_was_toggled(self, anyCheckName):
		print('Checked? ', anyCheckName)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()