def d_operator() :
  if operator == "+" :
    print (sum1+sum2)
  elif operator == "-" :
    print(sum1-sum2)
  elif operator == "*" :
    print(sum1*sum2)
  elif operator == "/" :
    print (sum1/sum2)

operation = input("Enter your operation : ")
n_loop = -1
for i in operation :
  n_loop +=1
  try :
    i = int(i)
  except ValueError :
    sum1 = int(operation [:n_loop])
    sum2 = int(operation [n_loop + 1 :])
    operator = i
d_operator()