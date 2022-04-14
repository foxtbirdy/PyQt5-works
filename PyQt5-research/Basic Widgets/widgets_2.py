import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qpixmap Image test")
        widget = QLabel("...")
        widget_1 = QLabel("QPixmap Image Testing with QLabel")
        widget.setPixmap(QPixmap("gfl_2.jpg"))
        widget.setScaledContents(False)
        widget_1.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)
        font = widget_1.font()
        font.setPointSize(10)
        widget_1.setFont(font)
        widget.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(widget)
        self.setMenuWidget(widget_1)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
