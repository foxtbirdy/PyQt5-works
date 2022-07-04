
the code of the QStackWidet is located on _Basic/layout_7/layout_7.py_.



# START


The QStackWidget is a feature that aids in the applications that consists of Tabbed features. Tabbed applications are developed using the technique of keeping the layouts of the applications in a single stack.

QStackWidget is fairly easy to use. the functionality is what is making this entire whole file look big. The concept of the QStackWidget is to add multiple different functionality to the application without the application to open up new windows every time.


The first step would be for the widgets to be added to the QStackWidget layout.

the code goes like this -

```
layout = QStackedLayout()

layout.addWidget(Color("red"))
layout.addWidget(Color("green"))
layout.addWidget(Color("blue"))
layout.addWidget(Color("yellow"))

```

According to the abilities of the layout, it is possible to arrange them into different styles and different designs which sounds interesting.

