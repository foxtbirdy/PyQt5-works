# Adding toolbar action's icon using QIcon and QSize for sizing that icon
# Martin Fitzpatrick's PyQt5 book didn't mentioned Qt, Qsize and other imports which resulted in confusion


import sys
import os
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
		toolBar.setIconSize(QSize(16,16)) # set size for all QToolbar icons
		self.addToolBar(toolBar)

		# I used svg formats because my png didn't work
		button_action = QAction(QIcon("PyQt5-research\Basic\images\png.svg"), "Button" , self)
		button_action.setStatusTip("Hello there")
		button_action.triggered.connect(self.toolBarClicked) 
		button_action.setCheckable(True)
		self.setStatusBar(QStatusBar(self))

		toolBar.addAction(button_action)



	def toolBarClicked(self,s):
		print("click", s)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
