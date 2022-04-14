from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QSize, Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("The app")

        self.button_is_checked = True
        self.button = QPushButton("Press me!")
        self.button.setCheckable(True)
        self.button.released.connect(self.the_button_was_released)
        self.button.setChecked(self.button_is_checked)
        self.setMaximumSize(1500, 1200)
        self.setFixedSize(QSize(400, 300))  # set the size
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        print("Clicked!")

    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()
        print(self.button_is_checked)

    def clicked_action(self):
        print("Clicked")

    def was_clicked(self):
        self.clicked_action = self.button.isChecked()

    def clicked_action_toggled(self):
        print("Clicked")


# Instance required
app = QApplication(sys.argv)

window = MainWindow()
window.show()  # hidden by default


app.exec_()  # start the event loop
