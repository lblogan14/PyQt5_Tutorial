import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class _Bar(QtWidgets.QWidget):

	# we can click the value on the Bar widget to get the value we want
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

	def _calculate_clicked_value(self, e):
		parent = self.parent()
		vmin, vmax = parent.minimum(), parent.maximum()
		d_height = self.size().height() + (self._padding * 2)
		step_size = d_height / self.n_steps
		click_y = e.y() - self._padding - step_size / 2

		pc = (d_height - click_y) / d_height
		value = vmin + pc * (vmax - vmin)
		self.clickedValue.emit(int(value))

	def mouseMoveEvent(self, e):
		self._calculate_clicked_value(e)

	def mousePressEvent(self, e):
		self._calculate_clicked_value(e)


class PowerBar(QtWidgets.QWidget):
	'''Custom Qt Widget to show a power bar and dial.
	demonstrating compund and custom-drawn widget

	Left-clicking the button shows the color-choose, while
	Right-clicking resets the color to None (no-color)
	'''

	colorChanged = QtCore.pyqtSignal()

	def __init__(self, steps=5, *args, **kwargs):
		super().__init__(*args, **kwargs)

		layout = QtWidgets.QVBoxLayout()
		self._bar = _Bar(steps)
		layout.addWidget(self._bar)

		# Create the QDial widget and set up defaults
		# we provide accessors on this class to override
		self._dial = QtWidgets.QDial()
		self._dial.setNotchesVisible(True)
		self._dial.setWrapping(False)
		self._dial.valueChanged.connect(self._bar._trigger_refresh)

		# Take feedback from click events on the meter
		self._bar.clickedValue.connect(self._dial.setValue)

		layout.addWidget(self._dial)
		self.setLayout(layout)

	def __getattr__(self, name):
		if name in self.__dict__:
			return self[name]

		return getattr(self._dial, name)

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

	def __getattr__(self, name):
		if name in self.__dict__:
			return self[name]

		try:
			return getattr(self._dial, name)
		except AttributeError:
			raise AttributeError(
				"'{}' object has no attribute '{}'".format(
					self.__class__.__name__, name))

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