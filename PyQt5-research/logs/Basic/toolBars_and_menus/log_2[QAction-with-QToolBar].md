

# START

The concept of the QAction is to a new method of adding actions whenever it is interacted. Let me rephase, the QAction instructs the library that a definite action had occured in the application. the library would direct the action to the specified functions.


The code is given below - 


```
button_action = QAction("Button", self)
button_action.setStatusTip("This is your button")
button_action.triggered.connect(self.toolbarClick)

toolbar.addAction(button_action)

```

The signals are started from the QAction. The first thing is to define the signals themselves. there are two instance of the QAction called text and a icon. Yes, we can add icon to the QAction thou it makes no sense to me.

The QAction is used for abstract user interfereces. it is a meaning that multiple interferece can be introduced in a single object. 

An example is like the Cut and the copy shortcuts on the keyboard. If you have those, then why would you even decided to create a new different functionality for it?