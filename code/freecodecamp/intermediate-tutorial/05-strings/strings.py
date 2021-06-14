# Strings: ordered, immutable, text representation 
my_string = "I'm  a programmer"

my_string = """Hello \
World""" 
print(my_string) 

my_string = "Hello World" 
char = my_string[0] 
print(char) 

# my_string[0] = 'h' 

substring = my_string[1:5] 
print(substring) 

substring = my_string[::2] 
print(substring) 

substring = my_string[::-1] 
print(substring) 

greeting = "Hello" 
name = "Tom" 
sentence = greeting + " " + name 
print(sentence) 

for x in greeting: 
    print(x) 

greeting = "Hello" 
if 'e' in greeting: 
    print('yes') 
else: 
    print('no') 

my_sting = '    Hello World     '  
my_string = my_string.strip() 
print(my_string) 

my_string = 'Hello World' 
print(my_string.lower()) 
print(my_string.endswith('Hello')) 
print(my_string.find('lo')) 
print(my_string.find('pp')) 
print(my_string.count('p')) 
print(my_string.replace('World', 'Universe')) 
print(my_string.replace('Worrrrld', 'Universe')) 

my_string = 'how are you doing' 
my_list = my_string.split(" ") 
print(my_list) 

my_string = 'how,are,you,doing' 
my_list = my_string.split(",") 
print(my_list) 

my_string = 'how,are,you,doing' 
my_list = my_string.split(",") 
print(my_list) 
new_string = ' '.join(my_list) 
print(new_string) 

from timeit import default_timer as timer 
my_list = ['a'] * 1000000

# bad 
start = timer() 
my_string = '' 
for i in my_list: 
    my_string += i 
stop = timer() 
print(stop-start) 

#good 
start = timer() 
my_string = ''.join(my_list) 
stop = timer() 
print(stop-start) 

# %, .format(), f-Strings 
var = "Tom" 
my_string = "the variable is %s" % var 
print(my_string) 

var = 3.1234567 
my_string = "the variable is %.2f" % var 
print(my_string) 

var = 3.1234567 
my_string = "the variable is {}".format(var) 
print(my_string) 

var = 3.1234567 
var2 = 6 
my_string = f"the variable is {var*2} and {var2}"
print(my_string) 

