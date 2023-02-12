import sys, os
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar, QAction, QStatusBar, QCheckBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle(os.path.basename(__file__)) # set name to self
        
        label = QLabel("Hello")
        label.setAlignment(Qt.AlignCenter)
        
        self.setCentralWidget(label)
        
        toolBar = QToolBar("Main Toolbar")
        toolBar.setIconSize(QSize(16,16)) # set Icon sizes for all toolBar icons
        self.addToolBar(toolBar)
        
        button_action = QAction(QIcon("extra/bug.png"), "&First Button", self) # & is more like nbsp which adds paddings
        button_action.setStatusTip("This is the first button that you wrote") # Display help text if mouse hovers over the toolBar icon
        button_action.triggered.connect(self.changeLabel)
        button_action.setCheckable(True) # Button is basically a checkbox as well
        toolBar.addAction(button_action)

        toolBar.addSeparator()
        
        button_action_2 = QAction(QIcon("extra/bug.png"), "&Second Button", self) # & is more like nbsp which adds paddings
        button_action_2.setStatusTip("This is the second button that you wrote") # Display help text if mouse hovers over the toolBar icon
        button_action_2.triggered.connect(self.changeTitle)
        button_action_2.setCheckable(True) # Button is basically a checkbox as well
        toolBar.addAction(button_action_2)

        toolBar.addWidget(QLabel("hello"))
        toolBar.addWidget(QCheckBox())
        
        self.setStatusBar(QStatusBar(self))
        
        menu = self.menuBar()
        
        file_menu = menu.addMenu("&File")
        file_menu.addAction(button_action)
        
    
    def changeLabel(self):
        print("Label was changed")
    
    
    def changeTitle(self):
        print("Title was changed")
        
    
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()