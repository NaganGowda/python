# finding prime numbers from 1 to 100

list_a = []

for i in range(2, 101) :
    list_a.append(i)
    
prime_numbers = []   
for a in list_a :
    prime = False
    for k in range(2, a):
        if (a%k) == 0 :
            prime = True
            break
    if not(prime) :
        prime_numbers.append(a)
print(prime_numbers)      


#star pyramid pattern

n = 10 

for i in range(1, n+1) :
    p = "* " * i
    left_space = " " * (n-i)
    print(left_space + p)        