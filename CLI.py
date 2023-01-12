while True :
    calculation = str(input("Please input your calculation : "))
    result = str(eval(calculation))
    print(f"result is {result}\n")
    completion = str(input("c to continue or another letter for exit :  "))
    if completion.lower() == "c" :
        print()
        continue
        
    else :
        break