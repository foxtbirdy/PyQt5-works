

# CUSTOM DIALOGS

```
class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Visit my Github Page!")
        self.setFixedSize(400,200)


        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("Visit me on my Github Page? \nClick Yes and the Webbrowser shall give you a ride!")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
```

This is the code that leads to creating a custom dialog page. the process is fairly simple. i think

the next thing to remember is that there is a slight bug here that i faced. it is related to class inheritence. since the mainwindow class was the parent, the class's code would be something like this - 

```
dlg = CustomDialog()

if dlg.exec_():
    webbrowser.open(url)
else:
    print("Redirection Cancelled.")
    app.quit() # exit the program
```

this is where the ```dlg = CustomDialog()``` was supposed to be ```dlg = CustomDialog(self)```. Please be careful.


# QMessageBox

the message dialogs with QmessageBox is the basics of every applications notification when they pop up. this is used for the purpose of notifying users with a slight notifications related to something.