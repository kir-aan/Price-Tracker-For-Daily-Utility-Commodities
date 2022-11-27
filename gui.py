from main import amazonSearch, kohlsSearch, walmartSearch
import webbrowser
from tkinter import *

def add_elements(frame: Frame, brand, productName, productPrice, productLink):

    pos = [0,0,200,5,200,70,550,65] # l1x, l1y, l2x, l2y, l3x, l3y, bx, by

    global label1
    label1=Label(master=frame, text=brand)
    label1.place(x=pos[0], y=pos[1])

    global label2
    label2 = Label(master=frame,text="Product Name: " + productName, wraplength=450)
    label2.place(x=pos[2], y=pos[3])

    global label3
    label3 = Label(master=frame, text="Product Cost: $"+(str)(productPrice))
    label3.place(x=pos[4],y=pos[5])

    #link productLink to link button
    global button
    button = Button(master=frame,
        text="Link",
        padx = 2,
        pady = 2,
        command= lambda : webbrowser.open_new(productLink)
    )
    button.place(x=pos[6],y=pos[7])

def search(event=None):
    search_query = query.get()
    amzSearchResult = amazonSearch(search_query)
    kohlSearchResult = kohlsSearch(search_query)
    walSearchResult = walmartSearch(search_query)
    frame1 = Frame(master=window, width=660, height=100, bg="light grey")
    frame1.place(x=20, y=100)

    frame2 = Frame(master=window, width=660, height=100, bg="light grey")
    frame2.place(x=20, y=220)

    frame3 = Frame(master=window, width=660, height=100, bg="light grey")
    frame3.place(x=20, y=340)
    add_elements(frame1, "Amazon", amzSearchResult[0], amzSearchResult[1], amzSearchResult[2])
    add_elements(frame2, "Kohls", kohlSearchResult[0], kohlSearchResult[1], kohlSearchResult[2])
    add_elements(frame3, "Walmart", walSearchResult[0], walSearchResult[1], walSearchResult[2])
    query.set("")


window = Tk()
window.title('Price Tracker For Daily Utility Commodities')
window.geometry("700x500")
window.configure(bg='white')
window.resizable(width=False, height=False)
query = StringVar()
search_bar = Entry(window,textvariable = query, font=('calibre',20,'normal'))
search_query = query.get()

search_button = Button(
    text="Search",
    padx = 2,
    pady = 2,
    command=search
    )

search_bar.place(x=180, y=25)
search_button.place(x=475, y=28)
window.bind('<Return>', search)
window.mainloop()