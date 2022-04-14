from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import Qt
import sys
from random import choice


window_titles = [
    'My App',
    'My App',
    'Still My App',
    'Still My App',
    'What on earth',
    'What on earth',
    'This is surprising',
    'This is surprising',
    'Something went wrong',
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.n_times_clicked = 0
        self.setWindowTitle("The 1st named App")

        self.button = QPushButton("Press me!")
        self.button.clicked.connect(self.the_button_got_clicked)
		self.windowTitleChanged.connect(self.the_title_changed)
        self.setCentralWidget(self.button)

    def the_button_got_clicked(self):
        print(f"Setting title : {choice(window_titles)}")
        self.setWindowTitle(choice(window_titles))

    def the_title_changed(self, window_title):
        print(f"Window title Changed: {window_title}")

        if window_title == "Something went wrong":
            self.button.setDisabled(True)


app = QApplication(sys.argv)

window = MainWindow()
window.show()


app.exec_()
