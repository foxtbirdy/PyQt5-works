# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2022-07-04 21:41:36
# @Last Modified by:   Climax
# @Last Modified time: 2022-07-04 23:42:03


import sys
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar, QAction, QStatusBar, QMenuBar, QCheckBox


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("Toolbars_and_menus_3.py")
		self.setFixedSize(600, 600)
		label = QLabel("Kon'nichiwa")
		label.setAlignment(Qt.AlignCenter)

		self.setCentralWidget(label)

		toolBar = QToolBar("Main toolbar")
		toolBar.setIconSize(QSize(25,25)) # set size
		toolBar.addWidget(QLabel("Click to check"))
		toolBar.addWidget(QCheckBox())
		self.addToolBar(toolBar)

		button_action = QAction(QIcon("extra/bug.png"),"Your button", self)
		button_action.setStatusTip("Hello there")
		button_action.setCheckable(True)
		button_action.triggered.connect(self.toolBarClicked) 
		toolBar.addAction(button_action)

		toolBar.addSeparator() # create a new toolbar action

		button_action_2 = QAction(QIcon("extra/bug.png"), "Your button", self)
		button_action_2.setStatusTip("Hello from Button 2")
		button_action_2.setCheckable(True)
		toolBar.addAction(button_action_2)


		self.setStatusBar(QStatusBar(self))

		menu = self.menuBar()

		file_menu = menu.addMenu("&File")
		file_menu.addAction(button_action)
		file_menu.addSeparator()
		file_menu.addAction(button_action_2)

		file_submenu = file_menu.addMenu("Submenu")
		file_submenu.addAction(button_action_2)



	def toolBarClicked(self,s):
		print("click", s)




app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
