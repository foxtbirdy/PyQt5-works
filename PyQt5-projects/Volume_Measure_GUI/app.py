# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2022-04-03 20:45:03
# @Last Modified by:   Climax
# @Last Modified time: 2022-04-04 19:30:18



import sys 

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDial, QLabel, QMainWindow
from PyQt5.QtGui import QFont


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("Volume Evaluation")
		self.setFixedSize(600, 400)
		self.Volume_Evaluation()
		self.dial()


	def dial(self):
		self.widget = QDial(self)
		self.widget.setGeometry(100,100,150,200) # x,y,w,h
		self.widget.setRange(0,100)
		self.widget.setSingleStep(1) # set keyboard input to 1 step
		self.widget.setSliderPosition(0) # set pos to 0
		self.widget.valueChanged.connect(self.value_changed)

	def Volume_Evaluation(self):
		self.text_label = QLabel("Move Dial to Evaluate", self)
		self.text_label.setGeometry(260,150,320,100) # x,y,w,h
		self.text_label.setFont(QFont('Arial', 15))

	def value_changed(self, i):
		if i==0:  self.text_label.setText(f"Current value[{i}]: Muted")
		if i>0:self.text_label.setText(f"Current value[{i}]: Very Low")
		if i>=20: self.text_label.setText(f"Current value[{i}]: Low")
		if i>=45: self.text_label.setText(f"Current value[{i}]: Medium")
		if i>=80: self.text_label.setText(f"Current value[{i}]: High")
		if i==100: self.text_label.setText(f"Current value[{i}]: Max")
		print(i)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()