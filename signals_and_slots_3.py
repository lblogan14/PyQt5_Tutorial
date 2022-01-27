import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from random import choice

window_titles = ['My App', 'Still my app', 'What on earch', 'This is surprising', 'Something went wrong']

# subclass QMainWindow to customize our application's main window
class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.n_times_clicked = 0

		self.setWindowTitle('My signal/slot app')

		self.button = QPushButton('Press me!')
		self.button.clicked.connect(self.the_button_was_clicked)

		# hook up the slot method 'the_window_title_changed' to the window signal '.windowTitleChanged'
		self.windowTitleChanged.connect(self.the_window_title_changed)

		self.setCentralWidget(self.button)

	def the_button_was_clicked(self):
		print('Clicked')
		new_window_title = choice(window_titles)
		print('Setting title: %s' % new_window_title)
		self.setWindowTitle(new_window_title) 

	def the_window_title_changed(self, window_title):
		print('Window title changed %s' % window_title)

		if window_title == 'Something went wrong':
			self.button.setDisabled(True)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()