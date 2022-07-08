#START


The dialogs are from the submodules of the PyQt5.QtWidget module "QDialog"

The dialogs are not like the main window. They act like the alert windows of any website. they are a kind of aysnchronos code where their user interaction forbids the users to use the application. they are used for open/save or settings, preferences, or features that doesn't fit the main application.

In Qt dialog boxes are handled by the QDialog class. To create a new dialog
box simply create a new object of QDialog type passing in a parent widget, e.g.
QMainWindow

That means if the ```__init__``` is set to ```parent=None`` or ```master=None``` then the program will not work. The cause would be a module import error or something.


This is the code to the simple dialog - 

```
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
class MainWindow(QMainWindow):
      def __init__(self):
          super().__init__()
          self.setWindowTitle("My App")
          button = QPushButton("Press me for a dialog!")
          button.clicked.connect(self.button_clicked)
          self.setCentralWidget(button)

          
      def button_clicked(self, s):
          print("click", s)

          dlg = QDialog(self)
          dlg.setWindowTitle("Hello")
          dlg.exec_() # excuete


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

```

It is recommended that you copy this code with the exceptions that there could be some indentation mistakes. be sure to fix them up.

