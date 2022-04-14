# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2022-04-14 21:18:53
# @Last Modified by:   Climax
# @Last Modified time: 2022-04-14 21:27:26


from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import QWidget



class Color(QWidget):
	def __init__(self, color):
		super().__init__()
		self.setAutoFillBackground(True)

		palette = self.palette()
		palette.setColor(QPalette.Window, QColor(color))
		self.setPalette(palette)
