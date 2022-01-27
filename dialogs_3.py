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
		dlg = QMessageBox(self)
		dlg.setWindowTitle('I have a question!')
		dlg.setText('This is a simple dialog')
		button = dlg.exec_()
		#dlg.setWindowTitle('HELLO!!')
		
		if button == QMessageBox.Ok:
			print('OK!')



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()