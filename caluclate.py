from tkinter import *
def addnumbers():
 res=int(ei.get())+int(e2.get())
 res=int(ei.get())-int(e2.get())
 res=int(ei.get())*int(e2.get())
 res=int(ei.get())/int(e2.get())
 my Text.set(res)
 my Text.set(res1)
 my Text.set(res2)
 my Text.set(res3)
 result.config(TextVarible=myText)
 result1.config(TextVarible=myText1)
 result2.config(TextVarible=myText2)
 result3.config(TextVarible=myText3)
 master=Tk()
 master.geometry("400X400")
 myText=String Var()
 myText1=String Var()
 myText2=String Var()
 myText3=String Var()
 label(master,text="first").grid(row=0,Sticky=W)
 label(master,text="first").grid(row=2,Sticky=W)
 label(master,text="first").grid(row=3,Sticky=W)
 result=label(master,text="add")
 result grid(row=3,column=1,Sticky=W)
 result=label(master,text="sub")
 result grid(row=3,column=2,Sticky=W)
 result=label(master,text="mul")
 result grid(row=3,column=3,Sticky=W)
 result=label(master,text="div")
 result grid(row=3,column=4,Sticky=W)
 e1=Entry(master)
 e2=entry(master)
 e1.grid(row=1,column=1)
 e2.grid(row=1,column=1)
 b=Button(master,text="calculate",command=add Numbers)
 b.grid(row=0,column=2,column span=2,row span=2,sticky=W+E+N+S,pad x=5 pad y=5)
mainloop()
 










