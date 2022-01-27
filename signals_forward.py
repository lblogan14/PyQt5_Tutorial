import sys

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit

class MainWindow(QMainWindow):
	message = pyqtSignal(str) # signal emits a str

	def __init__(self):
		super().__init__()

		self.message.connect(self.my_custom_fn)

		le = QLineEdit('Enter some text')
		# connect signal to .emit,
		# we can forward the signal to the receiving signals listeners
		le.textChanged.connect(self.message.emit)

		self.setCentralWidget(le)

	def my_custom_fn(self, s):
		print(s)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()