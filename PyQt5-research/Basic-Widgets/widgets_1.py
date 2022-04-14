import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("You are already dead")
        widget = QLabel("Oma-yamo shnrn de yu")
        font = widget.font()
        font.setPointSize(30)

        widget.setFont(font)
        widget.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)

        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
