import tkinter as tk

main = tk.Tk()
main.title("calculator")
main.geometry("400x700")
main.resizable(width="False", height="False")

calculator = tk.StringVar()
result = tk.StringVar()
text = ""

def add(num_operation):
    global text
    text = text + num_operation
    calculator.set(text)

def equal_def():
    global text
    result0 = str(eval(text))
    result.set(result0)

def reset_def():
    global text
    text = ""
    calculator.set(text)
    result.set(text)




#frame
button_frame = tk.Frame(main)

#labels
input_label = tk.Label(main, textvariable=calculator, text=10, font=("Times", 24))
result_label = tk.Label(main, textvariable=result, font=("Times", 24))

#numbers buttons
num_0 = tk.Button(button_frame, text="0",  command=lambda: add("0"), font=("Times", 36))  
num_1 = tk.Button(button_frame, text="1",  command=lambda: add("1"), font=("Times", 36)) 
num_2 = tk.Button(button_frame, text="2",  command=lambda: add("2"), font=("Times", 36)) 
num_3 = tk.Button(button_frame, text="3",  command=lambda: add("3"), font=("Times", 36))  
num_4 = tk.Button(button_frame, text="4",  command=lambda: add("4"), font=("Times", 36)) 
num_5 = tk.Button(button_frame, text="5",  command=lambda: add("5"), font=("Times", 36)) 
num_6 = tk.Button(button_frame, text="6",  command=lambda: add("6"), font=("Times", 36))  
num_7 = tk.Button(button_frame, text="7",  command=lambda: add("7"), font=("Times", 36))  
num_8 = tk.Button(button_frame, text="8",  command=lambda: add("8"), font=("Times", 36))  
num_9 = tk.Button(button_frame, text="9",  command=lambda: add("9"), font=("Times", 36))  

#operators buttons
plus = tk.Button(button_frame, text="+",  command=lambda: add("+"), font=("Times", 36))  
minus = tk.Button(button_frame, text="-",  command=lambda: add("-"), font=("Times", 36))  
division = tk.Button(button_frame, text="/",  command=lambda: add("/"), font=("Times", 36))  
multiplication = tk.Button(button_frame, text="*",  command=lambda: add("*"), font=("Times", 36))  
dot = tk.Button(button_frame, text=".",  command=lambda: add("."), font=("Times", 36))                                                      
equal = tk.Button(button_frame, text="=",  command=equal_def, font=("Times", 36))  
reset = tk.Button(button_frame, text="AC",  command=reset_def, font=("Times", 36))  

#show buttons in frame

#row 1
num_7         .grid(row=1, column=1, padx=7, pady=5)
num_8         .grid(row=1, column=2, padx=7, pady=5)
num_9         .grid(row=1, column=3, padx=7, pady=5)
multiplication.grid(row=1, column=4, padx=7, pady=5)

#row 2
num_4   .grid(row=2, column=1, padx=7, pady=5)
num_5   .grid(row=2, column=2, padx=7, pady=5)
num_6   .grid(row=2, column=3, padx=7, pady=5)
division.grid(row=2, column=4, padx=7, pady=5)

#row 3
num_1.grid(row=3, column=1, padx=7, pady=5)
num_2.grid(row=3, column=2, padx=7, pady=5)
num_3.grid(row=3, column=3, padx=7, pady=5)
plus .grid(row=3, column=4, padx=7, pady=5,)

#row 4
num_0.grid(row=4, column=1, padx=7, pady=5)
dot  .grid(row=4, column=2, padx=7, pady=5)
equal.grid(row=4, column=3, padx=7, pady=5)
minus.grid(row=4, column=4, padx=7, pady=5)

#row 5
reset.grid(row=5, column=1, padx=7, pady=5)

#show button frome
button_frame.place(relx=0.5, rely=0.2, anchor="n")
#show input label
input_label.pack(side="top", anchor="w")
#show result label
result_label.pack(side="top", anchor="e")


main.mainloop()