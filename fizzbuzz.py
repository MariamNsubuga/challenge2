


def fizzbuzz():
    a=[]
    b=[]
    a=  input('Enter list of a:')
    b=  input('Enter list of b:') 
    
    #total length of the two strings   
    totallength = int(len(a)) + int(len(b))
   #condition that will lead us to an output Fizz if the combined   length of the lists is divisible by 3
    if totallength % 3 == 0:
      return 'Fizz'
   #condition that will lead us to an output Fizz if the combined length of the lists is divisible by 5  
    if totallength % 5 == 0:
      return 'Buzz'
#condition that will lead us to an output Fizz if the combined length of the lists is divisible by both 3 and 5 
    if totallength % 5 == 0 and totallength % 3 == 0:
      return 'FizzBuzz'
#condition that will lead us to an output Fizz if the combined length of the lists is not divisible by 3 or 5 0r both
    else:
      return totallength

print(fizzbuzz())
