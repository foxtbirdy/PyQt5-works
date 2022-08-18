
_if you are reading this log, it means that you have downlaoded the Qt Creator or the Qt Designer Studio and have created a simple ui file format for the experiment purposes._


# START


Now that there is a method of loading the ui file. But if someone wishes to have a complete python based file that also contains the ui, use the pyuic5 function.

_IDFK if u need to install it seperately._

```
$ pyuic5 mainwindow.ui -o MainWindow.py
```

I suppose that if the name of your ui file is mainwindow.ui then the result would be a "MainWindow.py"

Again, this is the code to assemble to file

```
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

```

