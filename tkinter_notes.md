# Tkinter, notes

freecodecamp.org
codemy.org

Tkinter Course, https://youtu.be/YXPyB4XeYLA

## Basic concepts

root window is the main window in which all other widgets are placed

root.mainloop(), is the main loop that looks for input triggers

always call mainloop as the last logical line of code in your program

everything else is a widget; label widget, input box widget etc

## Labels, Input Boxes (Entry), Buttons

`myLable = Label(root, text="abc")`
`myInputBox = Entry(root, width=10)`
`myButton = Button(root, text="abc", command=myFunction)`

to create a quit button;
```
myQuitButton = Button(root, text="Quit Program", command=root.quit)
myQuitButton.pack()
```

**input boxes**

`myInputBox.get()`, to get the contents of myInputBox
`myInputBox.insert(0, "abc")`, to insert contents into myInputBox
`myInputBox.delete(0, END)`, to delete the contents of myInputBox 
`root.title("myTitle")`, title of the root window

**pack or grid**
pack just dumps widgets on the screen, grid allows widgets to be arranged in a grid

`myWidget.pack()`
`myWidget.grid(row=0, column=0)`

note the grid is a relative grid such that if you put something in col 1 and something in col 3 but leave col 2 empty, it will display on screen as col 2 alongside col 1; in other words it doesn't interpret no entry as blank padding

`myLabel.grid_forget()`, removes myLabel from that grid position

**functions**
in Tkinter you can't pass parameters to a function as part of instantiating a Widget by calling command=myFunction(myParams); instead you must use Lambda e.g.:

`myButton = Button(root, text="abc", command=Lambda: myFunction(myParameters)`

`global varName`, creates a global variable called varName

## Icons, images

`root.iconbitmap("myicon.ico")` creates an app icon that appears in the top left hand of a window


**images**
you can use GIFs natively however to use jpg or png you need to import Pillow (a fork of the Python Image Library or PIL)

at the Command Line or Console, type `pip install Pillow`
to check that Pillow is installed, type `pip freeze`

`from PIL import ImageTk, Image`

then use `ImageTk` to insert images into your app

```
myImg = ImageTk.PhotoImage(Image.open("myimage.jpg"))
myLabelImg = Label(image=myImg)
myLabelImg.pack()
```

## Creating an application status bar
```
myStatus = Label(root, text="my status msg", bd=1, relief=SUNKEN, anchor=E)
myStatus.grid(row=x, column=y, columnspan=z, sticky=W+E)
```
where x, y & z are numbers represents grid position and the number of columns to span
sticky uses a compass concept e.g. W+E stretches the Label in this case from W to E across the screen

## Frames

```
myFrame = LabelFrame(root, text="my frame", padx=5, pady=5)
```
where padx and pady refer to the inside padding
```
myFrame.pack(padx=10, pady10)
```
and when packing padx and pady refer to the outside padding

to use the frame, instead of placing things into root, place into myFrame

## Radio Buttons

complicated; refree to 2.07 of the tutorial

