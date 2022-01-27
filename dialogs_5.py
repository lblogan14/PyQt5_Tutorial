import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle('My simple dialog app')

		button = QPushButton('Press me for a dialog!')
		button.clicked.connect(self.button_clicked)

		self.setCentralWidget(button)

	def button_clicked(self, s):
		button = QMessageBox.question(self, 'Question dialog', 'The longer message')


		# QMessageBox has many button types
		# and other icon constants
		
		if button == QMessageBox.Yes:
			print('Yes!')
		else:
			print('No!')



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()