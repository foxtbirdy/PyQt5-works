import sys
import resources
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtWidgets import QMenuBar , QMenu
from PyQt5.QtWidgets import QToolBar, QAction, QSpinBox
from PyQt5.QtGui import *
from functools import partial
text = """
先輩...大丈夫ですか?
Senpai? Are you all right?
"""

newIcon = QIcon(":file-new.svg")
##############################################
class Windows(QMainWindow):
	def __init__(self , parent=None):
		super().__init__(parent)
		self.setWindowTitle("Python Menu TEST")


################################################################
#################### GUI DESIGINING BELOW ######################
################################################################

		self.setStyleSheet("""

QMenuBar {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                      stop:0 lightgray, stop:1 lightblue);
    spacing: 3px; 
}


QMenuBar::item:selected { 
    background: #a8a8a8;
}

QMenuBar::item:pressed {
    background: #888888;
}

QMenu {
    background-color: #b2eab1; 
    border: 1px solid black;
}

QMenu::item {
    background-color: transparent;
}

QMenu::item:selected { 
    background-color: #4b7c58;
}

QToolBar {
    background: lightblue;
    spacing: 10px; 
}
			""")
################################################################
#################### GUI DESIGINING ABOVE ######################
################################################################

		self.resize(800, 600)
		self.centralWidget = QLabel(text)

		self.label_a = QLabel(text, self)
		self.label_a.setFont(QFont("Arial" , 15))


		self.centralWidget = self.label_a
		self.centralWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

		self.setCentralWidget(self.centralWidget)
		self._createAction_()
		self._MenuBar_()
		self._createToolBars_()
		self._ContextMenu_()
		self._connectActions()
		self.createStatusBar()

################# FEATURE ADDING BELOW ##################

	def _MenuBar_(self):
		menuBar = self.menuBar()
        # File menu
		fileMenu = QMenu("&File", self)
		menuBar.addMenu(fileMenu)

		fileMenu.addAction(self.newAction)
		fileMenu.addAction(self.openAction)
		fileMenu.addAction(self.saveAction)
		fileMenu.addSeparator()
		fileMenu.addAction(self.exitAction)

        # Edit menu
		editMenu = menuBar.addMenu("&Edit")
		editMenu.addAction(self.copyAction)
		editMenu.addAction(self.pasteAction)
		editMenu.addAction(self.cutAction)
		editMenu.addSeparator()
		fileMenu2 = editMenu.addMenu("Find and Replace")
		fileMenu2.addAction("Find ? ")
		fileMenu2.addAction("Replace ? ") 
        # Help menu
		helpMenu = menuBar.addMenu(QIcon(":help-content.svg"), "&Help")
		helpMenu.addAction(self.helpContentAction)
		helpMenu.addAction(self.aboutAction)
		self.openRecentMenu = fileMenu.addMenu("Open Recent")


	def _createToolBars_(self):
		fileToolBar = self.addToolBar("File")
		fileToolBar.setMovable(False)
		editToolBar = QToolBar("Edit" , self)


		self.addToolBar(editToolBar)

		# File Toolbars
		fileToolBar.addAction(self.newAction)
		fileToolBar.addAction(self.openAction)
		fileToolBar.addAction(self.saveAction)
		# Editing Toolbars
		editToolBar.addAction(self.copyAction)
		editToolBar.addAction(self.pasteAction)
		editToolBar.addAction(self.cutAction)
		# WIDGETS!!!
		self.FONTspinBox = QSpinBox()
		self.FONTspinBox.setFocusPolicy(Qt.WheelFocus)
		editToolBar.addWidget(self.FONTspinBox)

	def _createAction_(self):
		self.newAction = QAction(self)
		self.newAction.setText("&New")
		self.openAction = QAction("&Open...", self)
		self.saveAction = QAction("&Save", self)
		self.exitAction = QAction("&Exit", self)
		self.copyAction = QAction("&Copy", self)
		self.pasteAction = QAction("&Paste", self)
		self.cutAction = QAction("&Cut", self)
		self.helpContentAction = QAction("&Help Content", self)
		self.aboutAction = QAction("&About", self)
		# Icons for File Action
		self.newAction.setIcon(QIcon(":file-new.svg"))
		self.openAction = QAction(QIcon(":file-open.svg"), "&Open", self)
		self.saveAction = QAction(QIcon(":file-save.svg"), "Save" , self)
		# Icons for Edit Actions
		self.copyAction = QAction(QIcon(":edit-copy.svg"), "&Copy", self)
		self.pasteAction = QAction(QIcon(":edit-paste.svg"), "Paste", self)
		self.cutAction = QAction(QIcon(":edit-cut.svg"), "Cut", self)
		# Shortcuts?
		self.newAction.setShortcut("Ctrl+N")
		self.openAction.setShortcut("Ctrl+O")
		self.saveAction.setShortcut("Ctrl+S")
		self.copyAction.setShortcut(QKeySequence.Copy)
		self.pasteAction.setShortcut(QKeySequence.Paste)
		self.cutAction.setShortcut(QKeySequence.Cut)

		# Adding status.....

		self.newAction.setStatusTip("Create a new file?")
		self.newAction.setToolTip("Create?")

		self.openAction.setStatusTip("Open a new file?")
		self.openAction.setToolTip("Open?")

		self.saveAction.setStatusTip("Save the file?")
		self.saveAction.setToolTip("Save?")

		self.copyAction.setStatusTip("Copy something?")
		self.copyAction.setToolTip("Copy?")

		self.pasteAction.setStatusTip("Paste something?")
		self.pasteAction.setToolTip("Paste?")

		self.cutAction.setStatusTip("Move something?")
		self.cutAction.setToolTip("Move?")

		self.helpContentAction.setStatusTip("Help Content....")
		self.aboutAction.setStatusTip("About File....")





	def _ContextMenu_(self):
		self.centralWidget.setContextMenuPolicy(Qt.ActionsContextMenu)
		self.centralWidget.addAction(self.newAction)
		self.centralWidget.addAction(self.openAction)
		self.centralWidget.addAction(self.saveAction)
		self.centralWidget.addAction(self.copyAction)
		self.centralWidget.addAction(self.pasteAction)
		self.centralWidget.addAction(self.cutAction)

################################################################
################### SLOT CONNECTIONS BELOW #####################
################################################################

	def newFile(self):
		self.centralWidget.setText("""
			<i>User</i> Clicked <b>New File</b>, but where is the New File Feature?
			""")
	def openFile(self):
		self.centralWidget.setText("""
			<i>User</i> wants to <b>Open File</b>, but where is the in-app file browser?
			""")
	def saveFile(self):
		self.centralWidget.setText("How can you save when you didn't even write anything?")

	def copyContent(self):
		self.centralWidget.setText("<b>Copy chan</b> got GOT TRIGGERED?!")

	def pasteContent(self):
		self.centralWidget.setText("<b>Paste chan</b> got a Jackpot!!")

	def cutContent(self):
		self.centralWidget.setText("I'm sorry but we are not doing art here..")

	def helpContent(self):
		self.centralWidget.setText("<b>HELP chan</b> is out of Context?")

	def about(self):
		self.centralWidget.setText("READ THE <b>GITHUB</b>, LOL")


	def _connectActions(self):
		self.newAction.triggered.connect(self.newFile)
		self.openAction.triggered.connect(self.openFile)
		self.saveAction.triggered.connect(self.saveFile)
		self.exitAction.triggered.connect(self.close)
		# Connect Edit actions
		self.copyAction.triggered.connect(self.copyContent)
		self.pasteAction.triggered.connect(self.pasteContent)
		self.cutAction.triggered.connect(self.cutContent)	
		# Connect Help actions	
		self.helpContentAction.triggered.connect(self.helpContent)
		self.aboutAction.triggered.connect(self.about)
		# Connect Recent Open Files
		self.openRecentMenu.aboutToShow.connect(self.populate_the_recents)		

################################################################
################### SLOT CONNECTIONS ABOVE #####################
################################################################
	def populate_the_recents(self):
		self.openRecentMenu.clear()
		actions = []
		fileName = [f"File-{n}" for n in range(5)]
		for fileNames in fileName:
			action = QAction(fileNames, self)
			action.triggered.connect(partial(self.openRecentFile, fileNames))
			actions.append(action)
		self.openRecentMenu.addActions(actions)


	def openRecentFile(self, filename):
		self.centralWidget.setText(f"<b>{filename}</b> got opened?")

	def createStatusBar(self):
		self.statusBar = self.statusBar()
		self.setStatusBar(self.statusBar)
		Qlabel_text = QLabel("Open Sourced Project", self)
		self.statusBar.addPermanentWidget(Qlabel_text)



if __name__ == "__main__":
	app = QApplication(sys.argv)
	win = Windows()
	win.show()
	sys.exit(app.exec_())
