# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2022-08-12 01:47:27
# @Last Modified by:   Climax
# @Last Modified time: 2022-08-18 23:09:42


# Another method of setting up the UI if you wish to use the .py format instead of the ui one.
# The .ui format is more understandable thou.

import sys

from PyQt5 import QtWidgets, uic

from MainWindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self, *args, obj=None, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)
		self.setupUi(self)


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()


# execuete
app.exec_()