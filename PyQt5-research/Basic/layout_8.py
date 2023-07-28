# QStackedLayout: Tabbed Views Application.
# In Tabbed Views, only 1 widget is shown at a time

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QStackedLayout, QHBoxLayout, QVBoxLayout, QPushButton

from layout_colorwidget import Color

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("QStackedLayout Tabbed Views DEMO")

		main_layout = QHBoxLayout()
		button_layout = QVBoxLayout()
		self.stackLayout = QStackedLayout()

		main_layout.addLayout(button_layout) # The page's button would be a vertical layout
		main_layout.addLayout(self.stackLayout) # Set main layout to be stackedLayout.



		btn = QPushButton("red")
		btn.pressed.connect(self.tab_1_active)
		button_layout.addWidget(btn)

		btn = QPushButton("green")
		btn.pressed.connect(self.tab_2_active)
		button_layout.addWidget(btn)

		btn = QPushButton("blue")
		btn.pressed.connect(self.tab_3_active)
		button_layout.addWidget(btn)

		btn = QPushButton("purple")
		btn.pressed.connect(self.tab_4_active)
		button_layout.addWidget(btn)

		
		widget = QWidget()
		
		widget.setLayout(main_layout)
		self.setCentralWidget(widget)


		self.stackLayout.addWidget(Color("red"))
		self.stackLayout.addWidget(Color("green"))
		self.stackLayout.addWidget(Color("blue"))
		self.stackLayout.addWidget(Color("purple"))

	# Use setCurrentIndex to display the current focused widget over the stackedWidget.

	def tab_1_active(self):
		self.stackLayout.setCurrentIndex(0)

	def tab_2_active(self):
		self.stackLayout.setCurrentIndex(1)
		
	def tab_3_active(self):
		self.stackLayout.setCurrentIndex(2)
		
	def tab_4_active(self):
		self.stackLayout.setCurrentIndex(3)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()