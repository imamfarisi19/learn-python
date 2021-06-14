#Dictionary: Key-Value pairs, Unordered, Mutable 
mydict = {"name": "Max", "age": 28, "City": "New York"} 
print(mydict) 

mydict2 = dict(name="Mary", age=27, city="Boston") 
print(mydict2) 

value = mydict["name"] 
print(value) 

mydict["email"] = "max@xyz.com" 
print(mydict) 

mydict["email"] = "coolmax@xyz.com" 
print(mydict) 

del mydict["name"]
print(mydict)

mydict.pop("age")
print(mydict)

mydict.popitem() 
print(mydict) 

if "name" in mydict: 
    print(mydict["name"]) 

try: 
    print(mydict["name"]) 
except: 
    print("Error") 

for key in mydict: 
    print(key) 

for key in mydict.keys(): 
    print(key) 

for value in mydict.values(): 
    print(value) 

for key, value in mydict.items(): 
    print(key, value) 

mydict_cpy = mydict 
print(mydict_cpy) 

mydict_cpy = dict(mydict) 

mydict_cpy["email"] = "max@xyz.com" 
print(mydict_cpy) 
print(mydict) 


my_dict = {"name": "Max", "age": 28, "email":"max@xyz.com"} 
my_dict_2 = dict(name="Mary", age=27, city="Boston") 

my_dict.update(my_dict_2) 
print(my_dict) 

my_dict = {3: 9, 6: 36, 9: 81}
print(my_dict)

# value = my_dict[3] 
mytuple = (8, 7) 
mydict = {mytuple: 15} 
print(mydict) 

# mytuple = [8, 7]
# mydict = {mytuple: 15} 
# print(mydict) 

