# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2022-07-04 21:41:36
# @Last Modified by:   Climax
# @Last Modified time: 2022-07-04 22:24:25


import sys
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar, QAction, QStatusBar


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("Toolbars_and_menus_3.py")
		label = QLabel("Kon'nichiwa")
		label.setAlignment(Qt.AlignCenter)

		self.setCentralWidget(label)

		toolBar = QToolBar("Main toolbar")
		toolBar.setIconSize(QSize(16,16)) # set size
		self.addToolBar(toolBar)

		button_action = QAction(QIcon("extra/bug.png"),"Your button", self)
		button_action.setStatusTip("Hello there")


		button_action.triggered.connect(self.toolBarClicked) 
		toolBar.addAction(button_action)

		# Status bar Text checkable or not
		# Status bar Text is FALSE checkable by default
		button_action.setCheckable(True)




		self.setStatusBar(QStatusBar(self))

	def toolBarClicked(self,s):
		print("click", s)




app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
