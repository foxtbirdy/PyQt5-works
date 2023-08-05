# Yes, you can add a seperator over QMenu as well... and a Submenu over the menu

import sys, os
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar, QAction, QStatusBar, QCheckBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle(os.path.basename(__file__)) # set name to self
        
        self.label = QLabel("Hello")
        self.label.setAlignment(Qt.AlignCenter)
        
        self.setCentralWidget(self.label)
        
        toolBar = QToolBar("Main Toolbar")
        toolBar.setIconSize(QSize(16,16)) # set Icon sizes for all toolBar icons
        self.addToolBar(toolBar)
        
        button_action = QAction(QIcon("PyQt5-research\Basic\images\png.svg"), "&First Button", self) # & is more like nbsp which adds paddings
        button_action.setStatusTip("This is the first button that you wrote")
        button_action.triggered.connect(self.changeLabel)
        button_action.setCheckable(True)
        toolBar.addAction(button_action)

        toolBar.addSeparator()
        
        button_action_2 = QAction(QIcon("PyQt5-research\Basic\images\png.svg"), "&Second Button", self) # & is more like nbsp which adds paddings
        button_action_2.setStatusTip("This is the second button that you wrote")
        button_action_2.triggered.connect(self.changeTitle)
        button_action_2.setCheckable(True)
        toolBar.addAction(button_action_2)

        toolBar.addWidget(QLabel("hello"))
        toolBar.addWidget(QCheckBox())
        
        self.setStatusBar(QStatusBar(self))
        
        # QMenu Init
        menu = self.menuBar()
        
        # Setting up the QMenu
        file_menu = menu.addMenu("&File")
        file_menu.addAction(button_action)
        file_menu.addSeparator()
        file_menu.addAction(button_action_2)

        # Menu inside of a menu creates a nested menu
        file_submenu = file_menu.addMenu("Submenu")
        file_submenu.addAction(button_action_2)

    
    def changeLabel(self):
        self.label.setText("Hi there again")
        print("Label was changed")
    
    
    def changeTitle(self):
        self.setWindowTitle("Submenu app included")
        print("Title was changed")
        
    
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()