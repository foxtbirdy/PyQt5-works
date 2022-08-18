# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2022-08-12 01:47:27
# @Last Modified by:   Climax
# @Last Modified time: 2022-08-18 22:58:42


# standard method of setting up the GUI


import sys

from PyQt5 import QtWidgets, uic


app = QtWidgets.QApplication(sys.argv)

window = uic.loadUi("mainwindow.ui")
window.show()


# execuete
app.exec_()