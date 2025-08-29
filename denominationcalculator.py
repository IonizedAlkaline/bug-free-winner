from tkinter import *
window=Tk()
window.geometry("500x500")
window.title("Window")

label1=Label(window,text="Enter the amount")
label1.pack()

entry1=Entry(window)
entry1.pack()
def calculate():
    amount = int(entry1.get())
    note2000=amount//2000
    amount=amount%2000
    note500=amount//500
    amount=amount%500
    note100=amount//100
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e1.insert(END,note2000)
    e2.insert(END,note500)
    e3.insert(END,note100)
btn=Button(window,text="calculate",command=calculate)
btn.pack()

label2=Label(window,text="The notes are: ")
label2.pack()

l1=Label(window,text="2000")
l1.pack()

e1=Entry()
e1.pack()

l2=Label(window,text="500")
l2.pack()

e2=Entry()
e2.pack()

l3=Label(window,text="100")
l3.pack()

e3=Entry()
e3.pack()
window.mainloop()