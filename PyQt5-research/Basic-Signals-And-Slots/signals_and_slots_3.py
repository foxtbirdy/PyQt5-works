from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QSize, Qt
import sys
from random import choice

window_titles = [
    "My App",
    "THIS App",
    "Is this an App",
    "Don't Abuse A.I" 
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("The app")

        self.button = QPushButton("Press me!")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.the_button_was_clicked)
        self.setCentralWidget(self.button)
        self.button_is_checked = True
        self.windowTitleChanged.connect(self.windowTitleChangedNow) # if window title was changed, connect to the func arg
        self.setFixedSize(QSize(400, 300))  # set the size


    def the_button_was_clicked(self):
        print("Clicked!")
        new_window_title = choice(window_titles)
        print(f"Setting Title '{new_window_title}'")
        self.setWindowTitle(new_window_title)
        
        
    def windowTitleChangedNow(self, window_title):
        print(f"Window Title Was Changed to '{window_title}'")        
        if window_title == window_titles[3]: self.button.setDisabled(True)

# Instance required
app = QApplication(sys.argv)

window = MainWindow()
window.show()  # hidden by default


app.exec_()  # start the event loop
