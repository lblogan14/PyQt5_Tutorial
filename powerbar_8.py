import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class _Bar(QtWidgets.QWidget):

	clickedValue = QtCore.pyqtSignal(int)

	def __init__(self, steps, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setSizePolicy(
			# make sure it expands as far as possible
			QtWidgets.QSizePolicy.MinimumExpanding,
			QtWidgets.QSizePolicy.MinimumExpanding)

		if isinstance(steps, list):
			# list of colors
			self.n_steps = len(steps)
			self.steps = steps
		elif isinstance(steps, int):
			# int number of bars, defaults to red
			self.n_steps = steps
			self.steps = ['red'] * steps
		else:
			raise TypeError('steps must be a list or int')

		self._bar_solid_percent = 0.8
		self._background_color = QtGui.QColor('black')
		self._padding = 4.0 # n-pixel gap around edge

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
		vmin, vmax = dial.minimum(), dial.maximum()
		value = dial.value()

		# Define our canvas
		d_height = painter.device().height() - (self._padding * 2)
		d_width = painter.device().width() - (self._padding * 2)
		# Draw the bars
		step_size = d_height / self.n_steps
		bar_height = step_size * self._bar_solid_percent
		bar_spacer = step_size * (1 - self._bar_solid_percent) / 2
		# Calculate the y-stop position, from the value in range
		pc = (value - vmin) / (vmax - vmin)
		n_steps_to_draw = int(pc * self.n_steps)

		for n in range(n_steps_to_draw):
			brush.setColor(QtGui.QColor(self.steps[n]))
			rect = QtCore.QRect(
					int(self._padding),
					int(self._padding + d_height - ((n+1) * step_size) + bar_spacer),
					int(d_width),
					int(bar_height)
			)
			painter.fillRect(rect, brush)

		painter.end()

	def _trigger_refresh(self):
		self.update()


class PowerBar(QtWidgets.QWidget):
	'''Custom Qt Widget to show a power bar and dial.
	demonstrating compund and custom-drawn widget
	'''

	def __init__(self, steps=5, *args, **kwargs):
		super().__init__(*args, **kwargs)

		layout = QtWidgets.QVBoxLayout()
		self._bar = _Bar(steps)
		layout.addWidget(self._bar)

		self._dial = QtWidgets.QDial()
		#add the following line to update
		self._dial.valueChanged.connect(self._bar._trigger_refresh)
		layout.addWidget(self._dial)

		self.setLayout(layout)

	def setColor(self, color):
		self._bar.steps = [color] * self._bar.n_steps
		self._bar.update()

	def setColors(self, colors):
		self._bar.n_steps = len(colors)
		self._bar.steps = colors
		self._bar.update()

	def setBarPadding(self, i):
		self._bar._padding = int(i)
		self._bar.update()

	def setBarSolidPercent(self, f):
		self._bar._bar_solid_percent = float(f)
		self._bar.update()

	def setBackgroundColor(self, color):
		self._bar._background_color = QtGui.QColor(color)
		self._bar.update()

app = QtWidgets.QApplication(sys.argv)
#volume = PowerBar()
#volume.show()
bar = PowerBar(["#49006a", "#7a0177", "#ae017e", "#dd3497", "#f768a1",
"#fa9fb5", "#fcc5c0", "#fde0dd", "#fff7f3"])
bar.setBarPadding(2)
bar.setBarSolidPercent(0.9)
bar.setBackgroundColor('gray')
bar.show()

app.exec_()