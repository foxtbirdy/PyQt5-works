from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QSize, Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("The app")

        button = QPushButton("Press me!")
        self.setCentralWidget(button)


# Instance required
app = QApplication(sys.argv)

window = MainWindow()
window.show()  # hidden by default


app.exec_()  # start the event loop
