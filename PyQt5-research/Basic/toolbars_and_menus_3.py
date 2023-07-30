# QStatusBar is used to display text over the bottom left of the app
# QStatusBar is used for displaying current action on the app
# It can also display by hovering toolbar actions

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar, QAction, QStatusBar


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("Toolbars_and_menus_3.py")
		label = QLabel("Kon'nichiwa")
		label.setAlignment(Qt.AlignCenter)

		self.setCentralWidget(label)

		toolBar = QToolBar("Main toolbar")
		self.addToolBar(toolBar)

		button_action = QAction("Your button", self)
		button_action.triggered.connect(self.toolBarClicked) 

		# Setting the statusTip or "What to do if something hovers on this"
		button_action.setStatusTip("Hello there")
  
		toolBar.addAction(button_action)
		button_action.setCheckable(True)

		# Set statusBar over current class (QMainWindow)
		self.setStatusBar(QStatusBar(self))

	def toolBarClicked(self,s):
		print("click", s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
