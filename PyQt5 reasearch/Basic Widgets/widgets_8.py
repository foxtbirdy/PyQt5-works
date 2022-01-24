# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2022-01-24 06:41:31
# @Last Modified by:   Climax
# @Last Modified time: 2022-01-24 06:52:57


import sys

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("My App")
		self.setFixedSize(QSize(400, 300))
		widget = QSlider() # main widget
		self.setCentralWidget(widget)


		widget.setMinimum(-10) 
		widget.setMaximum(3)

		widget.setSingleStep(3) # interval of 3

		widget.valueChanged.connect(self.value_changed)
		widget.sliderMoved.connect(self.slider_position)
		widget.sliderPressed.connect(self.SliderActive)
		widget.sliderReleased.connect(self.SliderInactive)



	def value_changed(self,i):
		print("Index value: ", i)


	def slider_position(self, p):
		print("position:" , p)

	def SliderActive(self):
		print("Slider is active")

	def SliderInactive(self):
		print("Slider is Inactive")





app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

