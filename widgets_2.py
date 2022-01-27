import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle('My picture app')

		widget = QLabel()
		widget.setPixmap(QPixmap('cat.jpg'))
		# stretch and scale to fit the window completely
		widget.setScaledContents(True)

		self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()