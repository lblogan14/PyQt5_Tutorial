import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

# subclass QMainWindow to customize our application's main window
class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle('My First App')

		button = QPushButton('Press Me!')

		# set a fixed size
		self.setMinimumSize(QSize(400,100))


		# set the central widget of the window
		self.setCentralWidget(button) # place this button in the QMainWindow


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()