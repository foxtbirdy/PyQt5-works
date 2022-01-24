from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

# Instance required
app = QApplication(sys.argv)


window = QMainWindow()
window.show()  # hidden by default


app.exec_()  # start the event loop
