# Sets: unordered, mutable, no duplicates 
myset = {1, 2, 3, 1, 2} 
print(myset) 

myset = set([1, 2, 3])
print(myset) 

myset = set("Hello")  
print(type(myset)) 

myset = set()
myset.add(1)
myset.add(2)
myset.add(3)
myset.remove(3) 

print(myset) 

myset.discard(4) 
print(myset.pop()) 

myset.clear() 

for x in myset: 
    print(x) 
if 2 in myset: 
    print("yes") 

odds = {1, 3, 5, 7, 9} 
evens = {0, 2, 4, 6, 8} 
primes = {2, 3, 5, 7} 

u = odds.union(evens) 
print(u) 

i = odds.intersection(primes) 
print(i) 

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9} 
setB = {1, 2, 3, 19, 11, 12} 

diff = setA.difference(setB) 
print(diff) 

diff = setB.symmetric_difference(setA) 
print(diff) 

diff = setA.symmetric_difference(setB) 
print(diff) 

setA.update(setB) 
print(setA) 

setA.intersection_update(setB) 
print(setA) 

setA.difference_update(setB) 
print(setA) 

setA.symmetric_difference_update(setB) 
print(setA) 

setA = {1, 2, 3, 4, 5, 6} 
setB = {1, 2, 3} 
setC = {7, 8} 

print(setA.issubset(setB)) 
print(setB.issubset(setA)) 

print(setB.issuperset(setA)) 
print(setA.issuperset(setB)) 

print(setA.isdisjoint(setB)) 

setA = {1, 2, 3, 4, 5, 6} 
setB = setA 
print(setB) 

setB = setA.copy() 
setB.add(7) 
print(setB) 
print(setA) 

setB = set(setA) 
print(setB) 
print(setA) 

a = frozenset([1, 2, 3, 4])
a.remove(1) 
print(a) 
