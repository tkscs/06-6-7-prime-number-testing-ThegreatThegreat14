Number = 359916012598740083996400089999

def is_integer (Number):
    if Number % 1 == 0:
        return True
    else:
        return False
    
def is_positive (Number):
    if Number > 0:
        return True
    else:
        return False
    
def is_divisible (Number, Divisor):
    if Number % Divisor == 0:
        return True
    else:
        return False
    
def is_prime (Number):
    prime_now = True
    if is_integer (Number) and is_positive (Number):
        if is_divisible (Number, 2):
                prime_now = False
                return ("Not_Prime")
        for i in range (3, Number//2 + 1, 2):
             if i % 10000000 == 0:
                 print(i)
             if is_divisible (Number, i):
                prime_now = False
                return ("Not_Prime")
    else:
        return ("Not_Prime")
    if prime_now == True:
        return ("Prime")

Answer = is_prime (Number)
    
print (Answer)
   