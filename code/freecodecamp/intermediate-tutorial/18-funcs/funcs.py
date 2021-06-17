'''
- The difference between arguments and parameters
- Positional and keyword arguments 
- Default arguments 
- Variable-length arguments (*args and **kwargs)
- Container unpacking into function arguments 
- Local vs. global arguments 
- Parameter passing (by value or by reference?) 

def print_name(name): 
    print(name) 

print_name('Alex') 



def foo(a, b, c, d=4): 
    print(a, b, c, d) 

# foo(c=1, b=2, a=3) 

foo(1, 2, 3, 7) 



def foo(a, b, *args, **kwargs): 
    print(a, b) 
    for arg in args: 
        print(arg) 
    for key in kwargs: 
        print(key, kwargs[key]) 

# foo(1, 2, 3, 4, 5, six=6, seven=7) 
# foo(1, 2, six=6, seven=7)
foo(1, 2, 3, 4) 



def foo(a, b, *, c, d): 
    print(a, b, c, d) 

foo(1, 2, c=3, d=4) 



def foo(*args, c, d): 
    print(c, d) 

foo(1, 2, 3, d=4) 



def foo(*args, last): 
    for arg in args: 
        print(arg) 
    print(last) 

foo(1, 2, 3, last=100) 



def foo(a, b, c): 
    print(a, b, c) 

#my_list=(0, 1, 2) 
my_dict = {'a': 1, 'b': 2, 'c': 3} 
foo(**my_dict) 



def foo(): 
    #global number 
    #x = number 
    number = 3 
    #print('number inside function:', x) 

number = 0 
foo() 
print(number) 
''' 
def foo(a_list): 
    #x = 5 
    a_list += [200, 300, 400] 
    #a_list = a_list + [200, 300, 400] 
    #a_list = [200, 300, 400] 
    #a_list.append(4) 
    #a_list[0] = -100 

#var = 10 
my_list = [1, 2, 3] 
#foo(var) 
foo(my_list) 
#print(var) 
print(my_list) 

