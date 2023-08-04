# Adding widgets to QToolBar


import sys
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar, QAction, QStatusBar, QCheckBox


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

		button_action_1 = QAction(QIcon("PyQt5-research\Basic\images\png.svg"),"Your button", self)
		button_action_1.setStatusTip("Hello there")
		button_action_1.setCheckable(True)
		button_action_1.triggered.connect(self.toolBarClicked) 
		toolBar.addAction(button_action_1)

		# Separator will separate the widgets by drawing a line
		toolBar.addSeparator()

		button_action_2 = QAction(QIcon("PyQt5-research\Basic\images\png.svg"), "Your button", self)
		button_action_2.setStatusTip("Hello from Button 2")
		button_action_2.setCheckable(True)
		toolBar.addAction(button_action_2)

		toolBar.addSeparator()
  
		toolBar.addWidget(QLabel("Hello"))

		toolBar.addSeparator()
  
		toolBar.addWidget(QCheckBox())

		self.setStatusBar(QStatusBar(self))

	def toolBarClicked(self,s):
		print("click", s)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
