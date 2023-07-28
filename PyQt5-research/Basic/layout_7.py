# QStackedLayout: Literally stacking multiple widgets in a single window.
# In this demo, the widgets are stacked but no way to prove it as no functionality is given.
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QStackedLayout

from layout_colorwidget import Color

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("QStackedLayout DEMO")

		layout = QStackedLayout()
		layout.addWidget(Color("red"))
		layout.addWidget(Color("green"))
		layout.addWidget(Color("blue"))
		layout.addWidget(Color("yellow"))

		layout.setCurrentIndex(0) # set current index



		widget = QWidget()
		widget.setLayout(layout)
		self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()