import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, 
							QHBoxLayout, QVBoxLayout, QWidget)

# import the Color class we just created
from layout_colorwidget import Color

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle('My Nesting layouts app')

		# generate different layouts
		layout1 = QHBoxLayout()
		layout2 = QVBoxLayout()
		layout3 = QVBoxLayout()

		# layout2 is vbox with 3 color block
		layout2.addWidget(Color('red'))
		layout2.addWidget(Color('yellow'))
		layout2.addWidget(Color('purple'))

		# layout3 is vbox with 2 color block
		layout3.addWidget(Color('red'))
		layout3.addWidget(Color('purple'))

		# layout1 includes layout2 as first block,
		# a color block as second hbox, and
		# layout3 as last hbox
		layout1.addLayout(layout2)
		layout1.addWidget(Color('green'))
		layout1.addLayout(layout3)


		widget = QWidget()
		widget.setLayout(layout1)

		self.setCentralWidget(widget)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()

# this will give us the border around the red widget,
# this is the layout spacing