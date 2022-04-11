from tkinter import *
from turtle import home
import pickle

class ShelfApp(Tk):
    def __init__(self, *args, **kwargs):
        # inherit from parent class
        Tk.__init__(self, *args, **kwargs)

        # create a container
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        # initialize frames
        self.frames = {}

        # iterate through the different frames
        for F in (Home, One, Two, Three, Four, Five, Six):
            frame = F(container, self)

            # add frames to the array
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")
        
        self.showFrame(Home)

    # display the current frame
    def showFrame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class ItemList():
    def __init__(self):
        self.items = []

    def __str__(self):
        s = ""
        for item in self.items:
            s += item + "\n"
        return s

    def addItem(self, entry, label):
        item = entry.get()
        self.items.append(item)
        label.delete(0, END)
        for i in range(len(self.items)):
            label.insert(i + 1, self.items[i])
        entry.delete(0, END)
    
    def removeItem(self, entry, label):
        item = entry.get()
        self.items.remove(item)
        label.delete(0, END)
        for i in range(len(self.items)):
            label.insert(i + 1, self.items[i])
        entry.delete(0, END)

try:
    with open("pickled_shelf_one.pickle", "rb") as f:
        shelf_one_items = pickle.load(f)
    with open("pickled_shelf_two.pickle", "rb") as f:
        shelf_two_items = pickle.load(f)
    with open("pickled_shelf_three.pickle", "rb") as f:
        shelf_three_items = pickle.load(f)
    with open("pickled_shelf_four.pickle", "rb") as f:
        shelf_four_items = pickle.load(f)
    with open("pickled_shelf_five.pickle", "rb") as f:
        shelf_five_items = pickle.load(f)
    with open("pickled_shelf_six.pickle", "rb") as f:
        shelf_six_items = pickle.load(f)

except FileNotFoundError:
    shelf_one_items = ItemList()
    shelf_two_items = ItemList()
    shelf_three_items = ItemList()
    shelf_four_items = ItemList()
    shelf_five_items = ItemList()
    shelf_six_items = ItemList()

class Home(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = Label(self, text ="Home Page")
        label.grid(row=0, column=2, padx=10, pady=10)

        button1 = Button(self, text="Shelf 1", background="pink", command = lambda: controller.showFrame(One))
        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = Button(self, text="Shelf 2", background="pink", command = lambda: controller.showFrame(Two))
        button2.grid(row=2, column=1, padx=10, pady=10)

        button3 = Button(self, text="Shelf 3", background="pink", command = lambda: controller.showFrame(Three))
        button3.grid(row=1, column=2, padx=10, pady=10)

        button4 = Button(self, text="Shelf 4", background="pink", command = lambda: controller.showFrame(Four))
        button4.grid(row=2, column=2, padx=10, pady=10)

        button5 = Button(self, text="Shelf 5", background="pink", command = lambda: controller.showFrame(Five))
        button5.grid(row=1, column=3, padx=10, pady=10)

        button6 = Button(self, text="Shelf 6", background="pink", command = lambda: controller.showFrame(Six))
        button6.grid(row=2, column=3, padx=10, pady=10)

        field = Entry(self)
        field.grid(row=3, column=0, padx=10, pady=10)

        search = Button(self, text="search shelves", command = lambda: self.searchItems(field, controller))
        search.grid(row=4, column=0, padx=10, pady=10)
    
    def searchItems(self, entry, controller):
        word = entry.get()
        if (word == "quit"):
            app.destroy()
        elif (word in shelf_one_items.items):
            controller.showFrame(One)
        elif (word in shelf_two_items.items):
            controller.showFrame(Two)
        elif (word in shelf_three_items.items):
            controller.showFrame(Three)
        elif (word in shelf_four_items.items):
            controller.showFrame(Four)
        elif (word in shelf_five_items.items):
            controller.showFrame(Five)
        elif (word in shelf_six_items.items):
            controller.showFrame(Six)
        entry.delete(0, END)

class One(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        
        title = Label(self, text="Shelf One")
        title.grid(row=0, column=4, padx=10, pady=10)

        home = Button(self, text="Home Page", command = lambda: controller.showFrame(Home))
        home.grid(row=1, column=1, padx=10, pady=10)

        items_label = Label(self, text=f"Items on Shelf One: ")
        items_label.grid(row=0, column=5, padx=10, pady=10)

        items = Listbox(self)
        items.grid(row=1, column=5, padx=10, pady=10)
        for i in range(len(shelf_one_items.items)):
            items.insert(i + 1, shelf_one_items.items[i])

        field = Entry(self)
        field.grid(row=2, column=0, padx=10, pady=10)

        add = Button(self, text="ADD", command = lambda: shelf_one_items.addItem(field, items))
        add.grid(row=3, column=0, padx=10, pady=10)

        grab = Button(self, text="REMOVE", command = lambda: shelf_one_items.removeItem(field, items))
        grab.grid(row=3, column=2, padx=10, pady=10)

class Two(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        title = Label(self, text="Shelf Two")
        title.grid(row=0, column=4, padx=10, pady=10)

        home = Button(self, text="Home Page", command = lambda: controller.showFrame(Home))
        home.grid(row=1, column=1, padx=10, pady=10)

        items_label = Label(self, text=f"Items on Shelf Two: ")
        items_label.grid(row=0, column=5, padx=10, pady=10)

        items = Listbox(self)
        items.grid(row=1, column=5, padx=10, pady=10)
        for i in range(len(shelf_two_items.items)):
            items.insert(i + 1, shelf_two_items.items[i])

        field = Entry(self)
        field.grid(row=2, column=0, padx=10, pady=10)

        add = Button(self, text="ADD", command = lambda: shelf_two_items.addItem(field, items))
        add.grid(row=3, column=0, padx=10, pady=10)

        grab = Button(self, text="REMOVE", command = lambda: shelf_two_items.removeItem(field, items))
        grab.grid(row=3, column=2, padx=10, pady=10)

class Three(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        title = Label(self, text="Shelf Three")
        title.grid(row=0, column=4, padx=10, pady=10)

        home = Button(self, text="Home Page", command = lambda: controller.showFrame(Home))
        home.grid(row=1, column=1, padx=10, pady=10)

        items_label = Label(self, text=f"Items on Shelf Three: ")
        items_label.grid(row=0, column=5, padx=10, pady=10)

        items = Listbox(self)
        items.grid(row=1, column=5, padx=10, pady=10)
        for i in range(len(shelf_three_items.items)):
            items.insert(i + 1, shelf_three_items.items[i])

        field = Entry(self)
        field.grid(row=2, column=0, padx=10, pady=10)

        add = Button(self, text="ADD", command = lambda: shelf_three_items.addItem(field, items))
        add.grid(row=3, column=0, padx=10, pady=10)

        grab = Button(self, text="REMOVE", command = lambda: shelf_three_items.removeItem(field, items))
        grab.grid(row=3, column=2, padx=10, pady=10)

class Four(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        title = Label(self, text="Shelf Four")
        title.grid(row=0, column=4, padx=10, pady=10)

        home = Button(self, text="Home Page", command = lambda: controller.showFrame(Home))
        home.grid(row=1, column=1, padx=10, pady=10)

        items_label = Label(self, text=f"Items on Shelf Four: ")
        items_label.grid(row=0, column=5, padx=10, pady=10)

        items = Listbox(self)
        items.grid(row=1, column=5, padx=10, pady=10)
        for i in range(len(shelf_four_items.items)):
            items.insert(i + 1, shelf_four_items.items[i])

        field = Entry(self)
        field.grid(row=2, column=0, padx=10, pady=10)

        add = Button(self, text="ADD", command = lambda: shelf_four_items.addItem(field, items))
        add.grid(row=3, column=0, padx=10, pady=10)

        grab = Button(self, text="REMOVE", command = lambda: shelf_four_items.removeItem(field, items))
        grab.grid(row=3, column=2, padx=10, pady=10)

class Five(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        title = Label(self, text="Shelf Five")
        title.grid(row=0, column=4, padx=10, pady=10)

        home = Button(self, text="Home Page", command = lambda: controller.showFrame(Home))
        home.grid(row=1, column=1, padx=10, pady=10)

        items_label = Label(self, text=f"Items on Shelf Five: ")
        items_label.grid(row=0, column=5, padx=10, pady=10)

        items = Listbox(self)
        items.grid(row=1, column=5, padx=10, pady=10)
        for i in range(len(shelf_five_items.items)):
            items.insert(i + 1, shelf_five_items.items[i])

        field = Entry(self)
        field.grid(row=2, column=0, padx=10, pady=10)

        add = Button(self, text="ADD", command = lambda: shelf_five_items.addItem(field, items))
        add.grid(row=3, column=0, padx=10, pady=10)

        grab = Button(self, text="REMOVE", command = lambda: shelf_five_items.removeItem(field, items))
        grab.grid(row=3, column=2, padx=10, pady=10)


class Six(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        title = Label(self, text="Shelf Six")
        title.grid(row=0, column=4, padx=10, pady=10)

        home = Button(self, text="Home Page", command = lambda: controller.showFrame(Home))
        home.grid(row=1, column=1, padx=10, pady=10)

        items_label = Label(self, text=f"Items on Shelf Six: ")
        items_label.grid(row=0, column=5, padx=10, pady=10)

        items = Listbox(self)
        items.grid(row=1, column=5, padx=10, pady=10)
        for i in range(len(shelf_six_items.items)):
            items.insert(i + 1, shelf_six_items.items[i])

        field = Entry(self)
        field.grid(row=2, column=0, padx=10, pady=10)

        add = Button(self, text="ADD", command = lambda: shelf_six_items.addItem(field, items))
        add.grid(row=3, column=0, padx=10, pady=10)

        grab = Button(self, text="REMOVE", command = lambda: shelf_six_items.removeItem(field, items))
        grab.grid(row=3, column=2, padx=10, pady=10)


app = ShelfApp()
app.title("The Shelfinator")
app.mainloop()
with open ("pickled_shelf_one.pickle", "wb") as f:
    pickle.dump(shelf_one_items, f)
with open ("pickled_shelf_two.pickle", "wb") as f:
    pickle.dump(shelf_two_items, f)
with open ("pickled_shelf_three.pickle", "wb") as f:
    pickle.dump(shelf_three_items, f)
with open ("pickled_shelf_four.pickle", "wb") as f:
    pickle.dump(shelf_four_items, f)
with open ("pickled_shelf_five.pickle", "wb") as f:
    pickle.dump(shelf_five_items, f)
with open ("pickled_shelf_six.pickle", "wb") as f:
    pickle.dump(shelf_six_items, f)
# =======

