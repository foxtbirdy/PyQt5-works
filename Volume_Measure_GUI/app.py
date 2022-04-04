# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2022-04-03 20:45:03
# @Last Modified by:   Climax
# @Last Modified time: 2022-04-04 17:36:28



import sys 

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDial, QLabel, QMainWindow
from PyQt5.QtGui import QFont


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("My App. A Dial Wheel")
		self.setFixedSize(600, 400)
		self.Volume_Evaluation()

		widget = QDial(self)
		

		widget.setGeometry(100,100,150,200) # x,y,w,h
		widget.setRange(0,100)
		widget.setSingleStep(1) # set keyboard input to 1 step
		widget.setSliderPosition(0) # set pos to 0
		widget.valueChanged.connect(self.value_Changed)

	def Volume_Evaluation(self):
		self.text_label = QLabel("testing", self)
		self.text_label.setGeometry(300,150,200,100) # x,y,w,h
		self.text_label.setFont(QFont('Arial', 15))

	def value_Changed(self, i):
		self.text_label.setText(f"Current value: {i}")
			


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()