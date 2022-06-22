import os
while True :
    sum1 = float(input("input the first number : "))
    
    operation = str(input("input the operation : "))
    
    sum2 = float(input("input the second number : "))
    
    if operation == "+" :
        print (sum1+sum2)
    
    if operation == "-" :
        print(sum1-sum2)
    
    if operation == "*" or operation == "×":
        print(sum1*sum2)
    
    if operation == "/" or operation =="÷":
        print (sum1/sum2)

    print()
    
    app = str (input(" c/e ,c to continue and will clear your screen , e to exit : "))
    app = app.lower()
    
    if app == "c" :
        os.system("clear")
        
    elif app =="e" :
        break
