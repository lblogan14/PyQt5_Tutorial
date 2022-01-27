import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton,
							QHBoxLayout, QVBoxLayout, QLabel, QWidget)

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		v = QVBoxLayout()
		h = QHBoxLayout()

		for a in range(10):
			button = QPushButton(str(a))
			# we accept the checked var on lambda but discard it
			# This button is not checkable, so it will always be False
			button.clicked.connect(lambda checked, val=a: self.button_clicked(val))
			h.addWidget(button)

		v.addLayout(h)
		self.label = QLabel('')
		v.addWidget(self.label)

		w = QWidget()
		w.setLayout(v)
		self.setCentralWidget(w)

	def button_clicked(self, n):
		self.label.setText(str(n))

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()