import tkinter as tk
import re
from tkinter import messagebox

main = tk.Tk()
main.title("calculator")
main.geometry("400x500")
main.resizable(width="False", height="False")

calculator = tk.StringVar()
result = tk.StringVar()
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
        messagebox.showerror("Error", "SyntaxError")

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

button_font = ("Helvetica 15 bold italic")
label_font =  ("Helvetica 15 bold italic")

#frame
button_frame = tk.Frame(main)

#labels
input_label = tk.Label(main, textvariable=calculator, font=label_font)
result_label = tk.Label(main, textvariable=result, font=label_font)

#numbers buttons
num_0 =           tk.Button(button_frame, text="0", width=5, height=2, font=button_font, command=lambda: add("0"))  
num_1 =           tk.Button(button_frame, text="1", width=5, height=2, font=button_font, command=lambda: add("1")) 
num_2 =           tk.Button(button_frame, text="2", width=5, height=2, font=button_font, command=lambda: add("2")) 
num_3 =           tk.Button(button_frame, text="3", width=5, height=2, font=button_font, command=lambda: add("3"))  
num_4 =           tk.Button(button_frame, text="4", width=5, height=2, font=button_font, command=lambda: add("4")) 
num_5 =           tk.Button(button_frame, text="5", width=5, height=2, font=button_font, command=lambda: add("5")) 
num_6 =           tk.Button(button_frame, text="6", width=5, height=2, font=button_font, command=lambda: add("6"))  
num_7 =           tk.Button(button_frame, text="7", width=5, height=2, font=button_font, command=lambda: add("7"))  
num_8 =           tk.Button(button_frame, text="8", width=5, height=2, font=button_font, command=lambda: add("8"))  
num_9 =           tk.Button(button_frame, text="9", width=5, height=2, font=button_font, command=lambda: add("9"))  

#operators buttons
plus =           tk.Button(button_frame, text="+" , width=5, height=5, font=button_font, command=lambda: add("+"))  
minus =          tk.Button(button_frame, text="-" , width=5, height=2, font=button_font, command=lambda: add("-"))  
division =       tk.Button(button_frame, text="÷" , width=5, height=2, font=button_font, command=lambda: add("÷"))  
multiplication = tk.Button(button_frame, text="×" , width=5, height=2, font=button_font, command=lambda: add("×"))  
percentage =     tk.Button(button_frame, text="%" , width=5, height=2, font=button_font, command=lambda: add("%"))  
dot =            tk.Button(button_frame, text="." , width=5, height=2, font=button_font, command=lambda: add("."))                                                      
equal =          tk.Button(button_frame, text="=" , width=5, height=2, font=button_font, command=equal_def)  
reset =          tk.Button(button_frame, text="AC", width=5, height=2, font=button_font, command=reset_def, )  
one_del =        tk.Button(button_frame, text="C" , width=5, height=2, font=button_font, command=one_del_def) 

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
plus .grid(row=4, column=4, padx=7, pady=5, rowspan=2)

#row 5
dot  .grid(row=5, column=1, padx=7, pady=5)
num_0.grid(row=5, column=2, padx=7, pady=5)
equal.grid(row=5, column=3, padx=7, pady=5)

#show button frome
button_frame.place(relx=0.5, rely=0.2, anchor="n")
#show input label
input_label.pack(side="top", anchor="w")
#show result label
result_label.pack(side="top", anchor="e")


main.mainloop()
