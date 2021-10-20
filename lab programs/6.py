import random
print("Random Functions")
x=int(input("Input x and y: "))
y=int(input())
print('Random interger between x and y =',random.randint(x,y),'\nRandom number = ',random.random(),'\nUniform(x and y) = ',random.uniform(x,y)
    ,'\nRandom range(x and y)= ', random.randrange(x,y))