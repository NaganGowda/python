# Chef and Chefina are playing with dice. In one turn, both of them roll their dice at once.

# They consider a turn to be good if the sum of the numbers on their dice is greater than 
# 6
# 6.
# Given that in a particular turn Chef and Chefina got 
# �
# X and 
# �
# Y on their respective dice, find whether the turn was good.




n = int(input())

for i in range(n):
    a = list(map(int,input().split()))
    sum_of_nums = sum(a)
    if sum_of_nums > 6 :
        print("Good")
    else :
        print("Not Good")