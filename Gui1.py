from tkinter import*
def add():
    f1=a.get()
    f2=b.get()
    s=f1+f2
    l3.config(text=s)
root=Tk()
root.geometry("400x400")
l1=Label(root,text="First Number")
l1.grid(row=0,column=0)
l2=Label(root,text="Second Number")
l2.grid(row=1,column=0)
l3=Label(root,text="The sum is:=")
a=IntVar()
b=IntVar()
e1=Entry(root,textvariable=a)
e1.grid(row=0,column=1)
e2=Entry(root,textvariable=b)
e2.grid(row=1,column=1)
btn=Button(root,text="Add",command=add)
btn.grid(row=2,column=1)
l3.grid(row=3,column=1)
root.mainloop()




