import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, 
							QStackedLayout, QPushButton, QVBoxLayout, QHBoxLayout)

# import the Color class we just created
from layout_colorwidget import Color

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle('My stacked button app')

		pagelayout = QVBoxLayout()
		button_layout = QHBoxLayout()
		self.stacklayout = QStackedLayout()

		pagelayout.addLayout(button_layout)
		pagelayout.addLayout(self.stacklayout)

		btn = QPushButton('red')
		btn.pressed.connect(self.activate_tab_1)
		button_layout.addWidget(btn)
		self.stacklayout.addWidget(Color('red'))

		btn = QPushButton('green')
		btn.pressed.connect(self.activate_tab_2)
		button_layout.addWidget(btn)
		self.stacklayout.addWidget(Color('green'))

		btn = QPushButton('yellow')
		btn.pressed.connect(self.activate_tab_3)
		button_layout.addWidget(btn)
		self.stacklayout.addWidget(Color('yellow'))

		widget = QWidget()
		widget.setLayout(pagelayout)

		self.setCentralWidget(widget)

	def activate_tab_1(self):
		self.stacklayout.setCurrentIndex(0)
	def activate_tab_2(self):
		self.stacklayout.setCurrentIndex(1)
	def activate_tab_3(self):
		self.stacklayout.setCurrentIndex(2)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()

# this will give us the border around the red widget,
# this is the layout spacing