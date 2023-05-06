# Chef got his dream seat in F1 and secured a # 3
# # �# 3 # rd
#   place in his debut race. He now wants to know the time gap between him and the winner of the race.
# You are his chief engineer and you only know the time gap between Chef and the runner up of the race, given as 
# �
# A seconds, and the time gap between the runner up and the winner of the race, given as 
# �
# B seconds.
# Please calculate and inform Chef about the time gap between him and the winner of the race.
n = int(input())

for i in range(n):
    (a, b) = list(map(int, input().split()))
    print(a+b)

# There is a fair going on in Chefland. Chef wants to visit the fair along with his �
# N friends. Chef manages to collect �
# K passes for the fair. Will Chef be able to enter the fair with all his �
# N friends?

# A person can enter the fair using one pass, and each pass can be used by only one person.

n = int(input())

for i in range(n):
    (a, b) = list(map(int, input().split()))
    if b>a :
        print("yes")
    else :
        print("no")


#pyramid code
n = int(input())

for i in range(1, n+1):
    space = (n-i) * " "
    print(space + "* " * i)

    