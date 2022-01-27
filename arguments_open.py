from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit

import sys

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.editor = QTextEdit()

		# remove script name
		# __file__ in sys.argv not work
		# because __file__ is the full filepath+filename
		scriptname = __file__.split('\\')[-1]
		if scriptname in sys.argv:
			print(scriptname in sys.argv)
			sys.argv.remove(scriptname)

		# if there is still something in sys.argv	
		if sys.argv:
			# take the 1st argument as filename
			filename = sys.argv[0]
			self.open_file(filename)
			

		self.setCentralWidget(self.editor)
		self.setWindowTitle('Text viewer')

	def open_file(self, fn):
		with open(fn, 'r') as f:
			text = f.read()

		self.editor.setPlainText(text)

app = QApplication(sys.argv)
w = MainWindow()
w.show()

app.exec_()