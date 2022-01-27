import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QSlider, QMainWindow

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle('My slider app')

		# to build a horizontal slider
		widget = QSlider(Qt.Horizontal)
		# vertical slider (by default)
		# widget = QSlider(Qt.Vertical)
		widget.setMinimum(-10)
		widget.setMaximum(10)
		# or: widget.setRange(-10, 10)
		widget.setSingleStep(3)

		widget.valueChanged.connect(self.value_changed)
		widget.sliderMoved.connect(self.slider_position)
		widget.sliderPressed.connect(self.slider_pressed)
		widget.sliderReleased.connect(self.slider_released)		

		self.setCentralWidget(widget)

	def value_changed(self, i):
		print('value is ', i)

	def slider_position(self, p):
		print('position is', p)

	def slider_pressed(self):
		print('Pressed!')

	def slider_released(self):
		print('Released!')


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()