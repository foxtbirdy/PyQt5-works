# QTabWidget: The other option of creating Tabbed Widgets without QSstackedWidget
# Only exception found yet is that QTabWidget is vertical. Why is that?

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTabWidget)

from layout_colorwidget import Color

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("Tabbed Edit + Box DEMO")

		tabs = QTabWidget()
		tabs.setDocumentMode(True) # for universal behavior
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