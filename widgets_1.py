import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle('My Widgets app')

		widget = QLabel('What\'s up')
		# get the current font
		font = widget.font()
		# modify the size
		font.setPointSize(50)
		# apply it back
		widget.setFont(font)

		# alignment is specified by a flag from Qt. namespace
		widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

		self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()