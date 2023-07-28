# Gridlayout based widget
# Range is determined by the highest row number or column number

import sys

from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import (
	QApplication,
	QLabel,
	QMainWindow,
	QWidget,
	QGridLayout
	)


from layout_colorwidget import Color



class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("QGridLayout ")
		self.setFixedSize(500,300)
		


		layout = QGridLayout()

		layout.addWidget(Color("red"),1,0) # 1 = row , 0 = column		layout.addWidget(Color("purple"),0,1)
		layout.addWidget(Color("green"),1,2)
		layout.addWidget(Color("blue"),2,1)
		layout.addWidget(Color("pink"),1,3)

		widget = QWidget()
		widget.setLayout(layout)

		self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
