
_if you are reading this log, it means that you have downlaoded the Qt Creator or the Qt Designer Studio and have created a simple ui for the experiment purposes._


# START

To be honest, I thought that the Qt Creator would take a lot of space but it didn't. I thought that it'll take 30 GBs but I only needed it for the desiging part of Desktop only. I scaled it down to 3 gigs. What a relief.


In the Qt Designer or the Qt Creator, the saved file of the designing part is usually called the ui format. The ui format is like a XML style based stylesheet crap that is so confusing to understand. Well, it is acceptable because this file is computer complied.

After creating the ui format, the task was to write a code that initializes the ui as its primary design of the GUI.

the pyqt5 has a module called the loadUi from the uic module "```uic.loadUi()```" and it worked flawlessly. the main code looks a lot cleaner than expected.

this is the code to load a ui file as the app gui

```

import sys

from PyQt5 import QtWidgets, uic


app = QtWidgets.QApplication(sys.argv)

window = uic.loadUi("mainwindow.ui")
window.show()


# execuete
app.exec_(

```

