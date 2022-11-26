from tkinter import *

window = Tk()
window.title('Price Tracker')
window.geometry("700x500")
window.configure(bg='white')
window.resizable(width=False, height=False)
query = StringVar()
search_bar = Entry(window,textvariable = query, font=('calibre',20,'normal'))
search_button = Button(
    text="Search",
    padx = 2,
    pady = 2
)
search_bar.place(x=180, y=25)
search_button.place(x=475, y=28)

frame1 = Frame(master=window, width=660, height=100, bg="light grey")
frame1.place(x=20, y=100)
amzLabel1 = Label(master=frame1, text="Amazon")
amzLabel1.place(x=0, y=0)
amzLabel2 = Label(master=frame1, text="Product Name: Yaheetech Office Chair")
amzLabel2.place(x=200, y=10)
amzLabel3 = Label(master=frame1, text="Product Cost: $29.99")
amzLabel3.place(x=200, y=35)
amzLinkButton = Button(master=frame1,
    text="Link",
    padx = 2,
    pady = 2
)
amzLinkButton.place(x=500, y=25)

frame2 = Frame(master=window, width=660, height=100, bg="light grey")
frame2.place(x=20, y=220)
tarLabel1 = Label(master=frame2, text="Target")
tarLabel1.place(x=0, y=0)
tarLabel2 = Label(master=frame2, text="Product Name: Costway Mid-Back Mesh Chair")
tarLabel2.place(x=200, y=10)
tarLabel3 = Label(master=frame2, text="Product Cost: $84.99")
tarLabel3.place(x=200, y=35)
tarLinkButton = Button(master=frame2,
    text="Link",
    padx = 2,
    pady = 2
)
tarLinkButton.place(x=500, y=25)

frame3 = Frame(master=window, width=660, height=100, bg="light grey")
frame3.place(x=20, y=340)
walLabel1 = Label(master=frame3, text="Walmart")
walLabel1.place(x=0, y=0)
walLabel2 = Label(master=frame3, text="Product Name: Adjustable Mid Back Mesh Chair")
walLabel2.place(x=200, y=10)
walLabel3 = Label(master=frame3, text="Product Cost: $49.99")
walLabel3.place(x=200, y=35)
walLinkButton = Button(master=frame3,
    text="Link",
    padx = 2,
    pady = 2
)
walLinkButton.place(x=500, y=25)

window.mainloop()

