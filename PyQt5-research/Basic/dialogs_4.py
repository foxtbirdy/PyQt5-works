# Using QMessage for message display other than QDialog


import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox

class MainWindow(QMainWindow):

	def __init__(self):
		super().__init__()
		self.setWindowTitle("App")


		# functionality
		button = QPushButton("Press me, get a dialog!")
		button.clicked.connect(self.button_clicked)
		self.setCentralWidget(button)

	def button_clicked(self, s):
		print('click', s)

		dlg = QMessageBox(self)


		dlg.setWindowTitle("Hey you there")

		dlg.setText("You are doing great right?")
  
		# Set icons for the message box
		dlg.setIcon(QMessageBox.Question)
		
		# Set event listener for QMessage Buttons response
		dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Ignore)
		
		button = dlg.exec_()
		
		# QMessage may have different buttons compared to QDialog
		if button == QMessageBox.Yes:
			print("Yes")
		elif button == QMessageBox.Ignore:
			print("He actually ignored me")




app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec_()

