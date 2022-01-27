import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle('My simple dialog app')

		button = QPushButton('Press me for a dialog!')
		button.clicked.connect(self.button_clicked)

		self.setCentralWidget(button)

	def button_clicked(self, s):
		dlg = QDialog(self)
		dlg.setWindowTitle('HELLO!!')
		dlg.exec_()
		#print('click', s)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()