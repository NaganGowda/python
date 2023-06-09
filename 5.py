
#star full pattern
n = 10 

for i in range(1, n+1) :
    p = "* " * i
    left_space = " " * (n-i)
    print(left_space + p) 
    
for i in range(1, n+1) :
    p = "* " * (n-i)
    left_space = " " * (i)
    print(left_space + p)