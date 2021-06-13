# List: ordered, mutable, allows duplicate eleements 
mylist = ["banana", "cherry", "apple"] 
print(mylist) 

item = mylist[2] 
print(item) 

for i in mylist: 
    print(i) 

if "banana" in mylist: 
    print("yes") 
else:
    print("no") 

print(len(mylist)) 

mylist.append("lemon") 
print(mylist) 

mylist.insert(1, "blueberry") 
print(mylist) 

item = mylist.pop() 
print(item) 
print(mylist) 

item = mylist.remove("cherry") 
print(item) 

mylist = [4, 3, 2, -1, 2, 10] 
item = mylist.sort() 
print(item) 

new_list = sorted(mylist) 
print(mylist) 
print(new_list) 

mylist = [0] * 5 
print(mylist) 

mylist2 = [1, 2, 3, 4, 5] 
new_list = mylist + mylist2 
print(new_list) 

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9] 

a = mylist[1:5] 
print(a) 

a = mylist[1::] 
print(a) 

a = mylist[2::] 
print(a) 

a = mylist[::-1] 
print(a) 

item = mylist.clear() 
print(item) 

list_org = ["bananna", "cherry", "apple"] 
list_cpy = list_org 
list_cpy.append("lemon") 
print(list_cpy) 
print(list_org) 

list_org = ["bananna", "cherry", "apple"] 
list_cpy = list_org.copy() 
list_cpy.append("lemon") 
print(list_cpy) 
print(list_org) 

list_org = ["bananna", "cherry", "apple"] 
list_cpy = list(list_org)
list_cpy.append("lemon") 
print(list_cpy) 
print(list_org) 

list_org = ["bananna", "cherry", "apple"] 
list_cpy = list_org[:] 
list_cpy.append("lemon") 
print(list_cpy) 
print(list_org) 

mylist = [1, 2, 3, 4, 5, 6] 
b = [i*i for i in mylist] 

print(mylist) 
print(b) 
