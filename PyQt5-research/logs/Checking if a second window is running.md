
In this log, I will be explaining the solution from Martin about to detect either a second window is already running or not.

### Why is it important?
The reason that its important is when you don't want to create a new window every time the user clicks the same button if the new window is already created. There are a number of ways to handle this issue.

1. [ NOT TESTED ] To disable the button feature if the second window is open.
2. [ TESTED ] To detect that the second window is running

The first option gives the code more readability but will require more code lines

The second option on the other hand gives less readability but lesser codelines are required.

I did not test the first option

### TESTING 2nd OPTION

Final code:

```

import sys
from random import randint  
from PyQt5.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget)




class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.w = None
		self.button = QPushButton("Click me for a widget to appear")
		self.button.clicked.connect(self.show_new_window)
		self.setCentralWidget(self.button)

	def create_window(self, clicked):
		print(clicked)
		self.w = AnotherWindow()
		self.w.show()


	def show_new_window(self, checked):
		print(checked)
		if self.w is None:
			self.w = AnotherWindow()
			self.w.show()




class AnotherWindow(QWidget):

	"""
	This is the window where there are no parents. it is a standalone widget of a sort
	"""
	def __init__(self):
		super().__init__()


		layout = QVBoxLayout()
		self.label = QLabel(
      f"Another Window with a random number: {randint(0,100)}"
      )

		self.button_exit = QPushButton("Click me to exit")
		self.button_exit.clicked.connect(self.exit_program)

		layout.addWidget(self.label)
		layout.addWidget(self.button_exit)
		
		self.setLayout(layout)


	def exit_program(self):
		app.quit()



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()


```

Over ```MainWindow``` class, there is an odd property called "w"
```
class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.w = None
		self.button = QPushButton("Click me for a widget to appear")
		self.button.clicked.connect(self.show_new_window)
		self.setCentralWidget(self.button)
```

If the second window is created, then ```self.w``` gets the ```AnotherWindow``` class.

If that occured then the code cannot create a new window unless the property variable is set to ```None``` again.

Finally this is the magic cake:

```
def show_new_window(self, checked):
	print(checked)
	if self.w is None:
		self.w = AnotherWindow()
		self.w.show()
```