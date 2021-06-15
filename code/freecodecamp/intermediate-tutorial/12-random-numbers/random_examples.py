import random 

# a = random.random() 
# a = random.uniform(1, 10) 
# a = random.randrange(1, 10) 
# a = random.normalvariate(0, 1) 
# print(a) 

# mylist = list("ABCDEFGH") 
# print(mylist) 

# a = random.choice(mylist) 
# a = random.sample(mylist, 3) 
# a = random.choices(mylist, k=3) 
# print(a) 

# mylist = list("ABCDEFGH") 
# random.shuffle(mylist) 
# print(mylist) 

'''
random.seed(1) 
print(random.random()) 
print(random.randint(1, 10))
random.seed(2) 
print(random.random()) 
print(random.randint(1, 10))

random.seed(1) 
print(random.random()) 
print(random.randint(1, 10))
random.seed(2) 
print(random.random()) 
print(random.randint(1, 10))
''' 
'''
import secrets 
mylist = list("ABCDEFGH") 
# a = secrets.randbelow(10) 
a = secrets.randbits(4)
#1111
print(a) 
'''
import numpy as np  

# a = np.random.rand(3, 3) 
# print(a) 

# a = np.random.randint(0, 10, (3, 4)) 
# print(a) 

arr = np.array([[1,2,3], [4,5,6], [7,8,9]]) 
print(arr) 
np.random.shuffle(arr) 
print(arr) 

np.random.seed(1) 
print(np.random.rand(3,3)) 
np.random.seed(1) 
print(np.random.rand(3,3)) 

