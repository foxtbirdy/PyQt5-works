

# START


The Tabbed Widget is a built-in function that is used for creating tabbed component based applications.

The code of the tabbed widget is.... very simple and it is quite straightforward. 

the module is to be imported.
in the tab widget, you can set the position on the north, south, east, west. the default is north.

North = Up.
West = left.
East = Right.
South = Down


The funny thing about this code is that the naming of the color widgets are done using a for loop. the code is written below - 

```
color_list = ["red", "green", "blue", "yellow"]
for n, color in enumerate(color_list):
    tabs.addTab(Color(color), color)

```

I could use the concept of the enumate on various other projects. There was a PDF converter project too. maybe I can work with and sorts.

The only downside that I found about this widget is that the tabs don't extend to the end of the window. Even if it is scallable, it looks more like a bad attention. What i mean to say is that this widget is not your toolbars or sorts.


