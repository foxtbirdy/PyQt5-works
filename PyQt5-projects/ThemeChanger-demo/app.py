# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2022-08-08 10:30:23
# @Last Modified by:   Climax
# @Last Modified time: 2022-08-08 11:20:44

import sys

from PyQt5.QtWidgets import (QMainWindow, QApplication, QToolBar, QAction)

class MainWindow(QMainWindow):
	

	def __init__(self):
		super().__init__()
		self.setWindowTitle("ThemeChanger")
		self.setFixedSize(500,300)

		button_color_red = QAction("Red", self)
		button_color_red.triggered.connect(self.change_theme_red)

		button_color_green = QAction("Green", self)
		button_color_green.triggered.connect(self.change_theme_green)

		button_color_blue = QAction("Blue", self)
		button_color_blue.triggered.connect(self.change_theme_blue)

		button_color_yellow = QAction("Yellow", self)
		button_color_yellow.triggered.connect(self.change_theme_yellow)

		menu = self.menuBar()
		customize_menu = menu.addMenu("Customize")
		theme_menu = customize_menu.addMenu("themes")

		theme_menu.addAction(button_color_red)
		theme_menu.addAction(button_color_green)
		theme_menu.addAction(button_color_blue)
		theme_menu.addAction(button_color_yellow)


	def change_theme_red(self):
		self.setStyleSheet("background-color: red")

	def change_theme_blue(self):
		self.setStyleSheet("background-color: blue")

	def change_theme_green(self):
		self.setStyleSheet("background-color: green")

	def change_theme_yellow(self):
		self.setStyleSheet("background-color: yellow")

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec_()