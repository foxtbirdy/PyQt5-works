from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QSize, Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("The app")

        button = QPushButton("Press me!")
        # button.setCheckable(False)
        button.clicked.connect(self.clicked_action)
        # self.setMaximumSize(1500, 1200)
        self.setFixedSize(QSize(400, 300))  # set the size
        self.setCentralWidget(button)

    def clicked_action(self):
        print("Clicked")


# Instance required
app = QApplication(sys.argv)

window = MainWindow()
window.show()  # hidden by default


app.exec_()  # start the event loop
