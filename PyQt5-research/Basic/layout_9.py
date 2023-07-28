# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2022-04-27 23:02:15
# @Last Modified by:   Climax
# @Last Modified time: 2022-04-30 01:28:54
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, QPushButton, QTabWidget,)

from layout_colorwidget import Color

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("Tabbed Edit + Box DEMO")

		tabs = QTabWidget()
		tabs.setTabPosition(QTabWidget.West)
		tabs.setMovable(True)

		color_list = ["red", "green", "blue", "yellow"]
		for n, color in enumerate(color_list):
			tabs.addTab(Color(color), color) # add color and the color name

		self.setCentralWidget(tabs)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()