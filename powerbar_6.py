import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class _Bar(QtWidgets.QWidget):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setSizePolicy(
			# make sure it expands as far as possible
			QtWidgets.QSizePolicy.MinimumExpanding,
			QtWidgets.QSizePolicy.MinimumExpanding)

	# this is the minimum size
	# make sure MinimumExpanding is used as well.
	def sizeHint(self):
		return QtCore.QSize(40, 120)

	def paintEvent(self, e):
		painter = QtGui.QPainter(self)

		brush = QtGui.QBrush()
		brush.setColor(QtGui.QColor('black'))
		brush.setStyle(Qt.SolidPattern)
		rect = QtCore.QRect(0, 0, painter.device().width(),
									painter.device().height())
		painter.fillRect(rect, brush)

		# Get current state
		dial = self.parent()._dial
		# line 31 uses .parent() to access the parent PowerBar widget
		# and through that the QDial via _dial.

		vmin, vmax = dial.minimum(), dial.maximum()
		value = dial.value()

		pen = painter.pen()
		pen.setColor(QtGui.QColor('red'))
		painter.setPen(pen)

		font = painter.font()
		font.setFamily('Times')
		font.setPointSize(18)
		painter.setFont(font)

		pc = (value - vmin) / (vmax - vmin)
		n_steps_to_draw = int(pc * 5)

		padding = 5
		# define our canvas
		d_height = painter.device().height() - (padding * 2)
		d_width = painter.device().width() - (padding * 2)
		# define each block size
		step_size = d_height / 5
		bar_height = step_size * 0.6
		bar_spacer = step_size * 0.4 / 2

		brush.setColor(QtGui.QColor('red'))

		for n in range(n_steps_to_draw):
			# QRect arguments: x, y, width, height
			rect = QtCore.QRect(
					padding,
					padding + d_height - ((n+1) * step_size) + bar_spacer,
					d_width,
					bar_height
			)
			painter.fillRect(rect, brush)

		painter.end()

	def _trigger_refresh(self):
		self.update()


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
		#add the following line to update
		self._dial.valueChanged.connect(self._bar._trigger_refresh)
		layout.addWidget(self._dial)

		self.setLayout(layout)

app = QtWidgets.QApplication(sys.argv)
volume = PowerBar()
volume.show()

app.exec_()