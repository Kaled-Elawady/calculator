from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import re


main = Tk()
main.title("calculator")
main.geometry("400x330")
main.resizable(width="False", height="False")

calculator = StringVar()
result = StringVar()
text = ""

def add(num_operation):
    global text
    if result.get() != "" :
        result.set("")
    text = text + num_operation
    calculator.set(text)

def equal_def():
    try:
        global text
        text = re.sub('^0*|(?<=[-\+\*/])0*', '', text) 
        text = text.replace("%", "*0.01")
        text = text.replace("×", "*")
        text = text.replace("÷", "/")
        
        text = str(eval(text))
        result.set(text)
        text = ""
    except SyntaxError : 
        showerror("Error", "SyntaxError")

def reset_def():
    global text
    text = ""
    calculator.set(text)
    result.set(text)

def one_del_def():
    global text
    if text == "" :
        None
    else :
        text = text.rstrip(text[-1])
        calculator.set(text)


label_style = Style().configure("TLabel", font = "Helvetica 20 bold italic")

button_style = Style().configure("TButton", font = "Helvetica 20 bold italic", width=5, height=2)
plus_style = Style().configure("b.TButton", font = "Helvetica 20 bold italic", width=5, height=5)


#frame
button_frame = Frame(main)

#labels
input_label = Label(main, textvariable=calculator, style=label_style)
result_label = Label(main, textvariable=result, style=label_style)

#numbers buttons
num_0 =           Button(button_frame, text="0" ,style="TButton",   command=lambda: add("0"))  
num_1 =           Button(button_frame, text="1" ,style="TButton",   command=lambda: add("1")) 
num_2 =           Button(button_frame, text="2" ,style="TButton",   command=lambda: add("2")) 
num_3 =           Button(button_frame, text="3" ,style="TButton",   command=lambda: add("3"))  
num_4 =           Button(button_frame, text="4" ,style="TButton",   command=lambda: add("4")) 
num_5 =           Button(button_frame, text="5" ,style="TButton",   command=lambda: add("5")) 
num_6 =           Button(button_frame, text="6" ,style="TButton",   command=lambda: add("6"))  
num_7 =           Button(button_frame, text="7" ,style="TButton",   command=lambda: add("7"))  
num_8 =           Button(button_frame, text="8" ,style="TButton",   command=lambda: add("8"))  
num_9 =           Button(button_frame, text="9" ,style="TButton",   command=lambda: add("9"))  

#operators buttons
plus =           Button(button_frame, text="+" ,style="b.TButton", command=lambda: add("+"))  
minus =          Button(button_frame, text="-" ,style="TButton",   command=lambda: add("-"))  
division =       Button(button_frame, text="÷" ,style="TButton",   command=lambda: add("÷"))  
multiplication = Button(button_frame, text="×" ,style="TButton",   command=lambda: add("×"))  
percentage =     Button(button_frame, text="%" ,style="TButton",   command=lambda: add("%"))  
dot =            Button(button_frame, text="." ,style="TButton",   command=lambda: add("."))                                                      
equal =          Button(button_frame, text="=" ,style="TButton",   command=equal_def)  
reset =          Button(button_frame, text="AC",style="TButton",   command=reset_def, )  
one_del =        Button(button_frame, text="C" ,style="TButton",   command=one_del_def) 

#show buttons in frame
#row 1
reset     .grid(row=1, column=1, padx=7, pady=5)
one_del   .grid(row=1, column=2, padx=7, pady=5)
percentage.grid(row=1, column=3, padx=7, pady=5)
division  .grid(row=1, column=4, padx=7, pady=5)

#row 2
num_7         .grid(row=2, column=1, padx=7, pady=5)
num_8         .grid(row=2, column=2, padx=7, pady=5)
num_9         .grid(row=2, column=3, padx=7, pady=5)
multiplication.grid(row=2, column=4, padx=7, pady=5)

#row 3
num_4.grid(row=3, column=1, padx=7, pady=5)
num_5.grid(row=3, column=2, padx=7, pady=5)
num_6.grid(row=3, column=3, padx=7, pady=5)
minus.grid(row=3, column=4, padx=7, pady=5)

#row 4
num_1.grid(row=4, column=1, padx=7, pady=5)
num_2.grid(row=4, column=2, padx=7, pady=5)
num_3.grid(row=4, column=3, padx=7, pady=5)
plus .grid(row=4, column=4, padx=7, pady=5, rowspan=2, ipady=20)

#row 5
dot  .grid(row=5, column=1, padx=7, pady=5)
num_0.grid(row=5, column=2, padx=7, pady=5)
equal.grid(row=5, column=3, padx=7, pady=5)

#show button frome
button_frame.place(relx=0.5, rely=0.22, anchor="n")
#show input label
input_label.pack(side="top", anchor="w")
#show result label
result_label.pack(side="top", anchor="e")


main.mainloop()
