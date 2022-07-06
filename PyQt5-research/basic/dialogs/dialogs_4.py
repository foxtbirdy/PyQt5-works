# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2022-07-06 16:25:20
# @Last Modified by:   Climax
# @Last Modified time: 2022-07-06 22:04:58



import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QDialog, QDialogButtonBox, QLabel, QMessageBox

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
		dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Ignore)
		dlg.setIcon(QMessageBox.Question)
		button = dlg.exec_()

		if button == QMessageBox.Yes:
			print("Yes")
		elif button == QMessageBox.Ignore:
			print("He actually ignored me")


class CustomDialog(QDialog):
	def __init__(self):
		super().__init__()



app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec_()

