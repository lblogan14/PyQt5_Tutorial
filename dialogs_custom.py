from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel
# We can subclass it to customize the QDialog
class CustomDialog(QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)

		self.setWindowTitle('HELLO!!')

		# can add more buttons with '|''
		QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

		self.buttonBox = QDialogButtonBox(QBtn)
		self.buttonBox.accepted.connect(self.accept)
		self.buttonBox.rejected.connect(self.reject)

		self.layout = QVBoxLayout()
		message = QLabel('Something happened, is that OK?')
		self.layout.addWidget(message)
		self.layout.addWidget(self.buttonBox)
		self.setLayout(self.layout)