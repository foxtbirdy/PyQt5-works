# Creating a Widget shortcut
# import and use as function to set color


from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import QWidget

class Color(QWidget):
	def __init__(self, color):
		super().__init__()
		self.setAutoFillBackground(True)

		palette = self.palette()
		palette.setColor(QPalette.Window, QColor(color))
		self.setPalette(palette)
