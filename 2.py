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



# In Chefland, everyone who earns strictly more than 
# Y rupees per year, has to pay a tax to Chef. Chef has allowed a special scheme where you can invest any amount of money and claim exemption for it.

# You have earned�X (�>�)
# (X>Y) rupees this year. Find the minimum amount of money you have to invest so that you don't have to pay taxes this year.



n = int(input())

for i in range(n):
    a = list(map(int,input().split()))
    result = a[0] - a[1]
    print(result)


# Recently, Chef visited his doctor. The doctor advised Chef to drink at least 
# 2000
# 2000 ml of water each day.

# Chef drank 
# �
# X ml of water today. Determine if Chef followed the doctor's advice or not.


t = int(input())

for a in range(t):
    a = int(input())
    if a >= 2000 :
        print("yes")
    else :
        print("no")



# Chef has been working hard to compete in MasterChef.
# He is ranked 
# �
# X out of all contestants. However, only 
# 10
# 10 contestants would be selected for the finals.

# Check whether Chef made it to the top 
# 10
# 10 or not?        


t = int(input())

for a in range(t):
    a = int(input())
    if a <= 10 :
        print("yes")
    else :
        print("no")