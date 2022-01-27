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
		# QMessageBox.question(parent, title, message)
		# if parent is main window, pass self
		# other methods are information, warning, critical, about
		button = QMessageBox.critical(
			self,
			'Oh dear!',
			'Something went very wrong!',
			buttons=QMessageBox.Discard | QMessageBox.NoToAll | QMessageBox.Ignore,
			defaultButton=QMessageBox.Discard)

		
		if button == QMessageBox.Yes:
			print('Yes!')
		else:
			print('No!')
		# no need to write more lines compared with dialogs_4
		# even exec_() is omitted.


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()