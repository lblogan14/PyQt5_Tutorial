from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import QWidget

class Color(QWidget):
	# Accept a single parameter when creating the widget - color (a str)
	def __init__(self, color):
		super().__init__()
		# automatically fill its background with window color
		self.setAutoFillBackground(True)

		palette = self.palette()
		# change the widget's QPalette.Window color to a new QColor
		# described by the value color passed in
		palette.setColor(QPalette.Window, QColor(color))
		# apply this palette back to widget
		self.setPalette(palette)