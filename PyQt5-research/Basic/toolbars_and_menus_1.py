# QToolBar: Creating a table that can be used to add more functionality
# Set QToolBar to Active window

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("QToolBar Demo")


		label = QLabel("Hello")
		label.setAlignment(Qt.AlignCenter)

		self.setCentralWidget(label)

		toolBar = QToolBar("ToolBar")
  
		# adding toolBar to app
		self.addToolBar(toolBar)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
