# Create a window
from PyQt5.QtWidgets import QApplication, QWidget

# only needed for access to command line arguments
import sys

# We Need one (and only one) QApplication instance per application.
# pass in sys.argv to allow command line arguments for the app.
# If we know we won't use command line arguments,
# use QAplication([]) instead
app = QApplication(sys.argv)

# create a Qt widget, which will be our window
window = QWidget()
window.show() # IMPORTANT! windows are hidden by default

# start the event loop
app.exec_()


# our app won't reach here until we exit and the event loop has stopped.