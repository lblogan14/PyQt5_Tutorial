import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

# import custom dialogs
from dialogs_custom import CustomDialog

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle('My simple dialog app')

		button = QPushButton('Press me for a dialog!')
		button.clicked.connect(self.button_clicked)

		self.setCentralWidget(button)

	def button_clicked(self, s):
		print('click', s)
		dlg = CustomDialog(self)
		#dlg.setWindowTitle('HELLO!!')
		
		if dlg.exec_():
			print('Success!')
		else:
			print('Cancel!')



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()