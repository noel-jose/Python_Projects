'''
       CREATING A CALCULATOR APPLICATION
'''
from tkinter import *

root = Tk()
root.title("Basic Calculator")

#created the input box
Input = Entry(root,width = 24,borderwidth = 2)
Input.grid(row = 0,column = 0,columnspan = 4,ipadx= 80,ipady = 15)

def on_click(num):
	Input.insert(END,str(num))

def clear():
	Input.delete(0,END)

def operation(sign):
        global first_num , Sign
        first_num = int(Input.get())
        Input.delete(0,END)
        Sign = sign
        

def buttonAdd():
        operation("+")
        

def buttonSub():
        operation("-")

def buttonMul():
        operation("*")

def buttonDiv():
        operation("/")

def buttonEqual():
        second_num = int(Input.get())
        Input.delete(0,END)
        if Sign == "+":
                Input.insert(0,first_num + second_num)
        if Sign == "-":
                Input.insert(0,first_num - second_num)
        if Sign == "*":
                Input.insert(0,first_num * second_num)
        if Sign == "/":
                Input.insert(0,first_num // second_num)

        
#creating buttons
Button1 = Button(root,text = "1",padx = 30,pady = 20,command = lambda: on_click(1))
Button2 = Button(root,text = "2",padx = 30,pady = 20,command = lambda: on_click(2))
Button3 = Button(root,text = "3",padx = 30,pady = 20,command = lambda: on_click(3))
Button4 = Button(root,text = "4",padx = 30,pady = 20,command = lambda: on_click(4))
Button5 = Button(root,text = "5",padx = 30,pady = 20,command = lambda: on_click(5))
Button6 = Button(root,text = "6",padx = 30,pady = 20,command = lambda: on_click(6))
Button7 = Button(root,text = "7",padx = 30,pady = 20,command = lambda: on_click(7))
Button8 = Button(root,text = "8",padx = 30,pady = 20,command = lambda: on_click(8))
Button9 = Button(root,text = "9",padx = 30,pady = 20,command = lambda: on_click(9))
Button0 = Button(root,text = "0",padx = 30,pady = 20,command = lambda: on_click(0))
Buttonplus = Button(root,text = "+",padx = 29,pady = 20,bg = "grey",command = buttonAdd)
Buttonequal = Button(root,text = "=",padx = 29,pady = 20,bg = "orange" ,command = buttonEqual)
Buttonmulti = Button(root,text = "*",padx = 30,pady = 20,bg = "grey",command = buttonMul)
Buttonsub = Button(root,text = "-",padx = 30,pady = 20,bg = "grey",command = buttonSub)
Buttondiv = Button(root,text = "/",padx = 30,pady = 20,bg = "grey",command = buttonDiv)
Buttonclear = Button(root,text = "CLR",padx = 22,pady = 20,bg = "grey",command = lambda:clear())

#putting the buttons on the screen
Button7.grid(row =1 ,column = 0)
Button8.grid(row =1 ,column = 1)
Button9.grid(row =1 ,column = 2)
Buttonclear.grid(row = 1,column = 3)

Button4.grid(row =2 ,column = 0)
Button5.grid(row =2 ,column = 1)
Button6.grid(row =2 ,column = 2)
Buttonsub.grid(row = 2,column = 3)

Button1.grid(row =3 ,column = 0)
Button2.grid(row =3 ,column = 1)
Button3.grid(row =3 ,column = 2)
Buttondiv.grid(row = 3,column = 3)

Buttonplus.grid(row =4 ,column = 0)
Button0.grid(row =4 ,column = 1)
Buttonequal.grid(row =4 ,column = 2)
Buttonmulti.grid(row = 4,column = 3)



root.mainloop()
