import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class _Bar(QtWidgets.QWidget):
	pass

class PowerBar(QtWidgets.QWidget):
	'''Custom Qt Widget to show a power bar and dial.
	demonstrating compund and custom-drawn widget
	'''

	def __init__(self, steps=5):
		super().__init__()

		layout = QtWidgets.QVBoxLayout()
		self._bar = _Bar()
		layout.addWidget(self._bar)

		self._dial = QtWidgets.QDial()
		layout.addWidget(self._dial)

		self.setLayout(layout)

app = QtWidgets.QApplication(sys.argv)
volume = PowerBar()
volume.show()

app.exec_()