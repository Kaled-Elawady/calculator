def d_operator() :
  if operator == "+" :
    print (sum1+sum2)
  elif operator == "-" :
    print(sum1-sum2)
  elif operator == "*" :
    print(sum1*sum2)
  elif operator == "/" :
    print (sum1/sum2)


while True :
  print()
  operation = input("Enter your operation : ")
  print()
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
  print()
  u_input = input("c to calculate another operation or any different key te exit : ") 
  if u_input == "c" :
    continue
  else :
    break