This is dedicated to the layout_2a of the PyQt5 QColor tutorial.



# START

The only common difference from the layout_1 and the layout_2a is the layout border. the layout is a feature that is used to arrange the widgets horizontally or vertically. 

The concept of the layout is that it is used to organized widgets. 
The reason that there is a border is because it looks like a border. the layout had been given the *Color* property. Therefore, the layout is the color while the widget is simply the main window itself.

The code is given below - 

```

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget

# import from local files
from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QColor demo")

        layout = QVBoxLayout()
        layout.addWidget(Color("red"))

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()

```


The layout according to the tutorial is called the Border spacing. Well, that's assuring.