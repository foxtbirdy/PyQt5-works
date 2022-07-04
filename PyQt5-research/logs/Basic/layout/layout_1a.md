The layout_1 is nothing special. However, after seeing the file structure made my mind exploded with ideas. If this type of code is used in future projects, I am certain that it'd score a lot when it comes to strcuturing the codefiles and as well as making the IO imports easier. Therefore, let's begin.


# START

The layout_1 uses two files for the app to work. 
    1. layout_1.py
    2. layout_colorwidget.py

I would be explaining them all both.


The *layout_colorwidget.py* is responsible for the color selection of the app. the main QColor and the QPalatte code are located here. The code is given below - 

```

from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import QWidget



class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

```

In this code, we use the QWidget to create a new custom widget called Color. The color is going to accept a single argument for choosing the name of the color. 

The *self.setAutoFillBackground(bool)* is a function that tells the program of QColor to automatically fill the widget with the color given. 

Configuring the palette would be hard to understand in a single line. Therefore, breaking it down is a good option. 
The palette is given as the self.palette(). the variable is given additional properties that include the setColor where the QPalette explains the window of the app and the QColor explains the color of the widget.

At the end of the code file, we simply self.setPalette(palette) ourselves.


The *layout_1.py* is simply easy to understand afterwards - 

```

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow

# import from local files
from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QColor demo")

        widget = Color("red")
        self.setCentralWidget(widget)



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
```

the widget is specified as the code of the previous code file and thus, the app is built!