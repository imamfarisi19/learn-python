def create_pyramid(rows): 
    for i in range(rows): 
        print(' ' * ( rows- i - 1 ) + '*' * ( 2 * i + 1))

print(create_pyramid(10))

def create_upside_down_pyramid(rows):
    for i in reversed(list(range(rows))):
        print(' ' * ( rows- i - 1 ) + '*' * ( 2 * i + 1))

print(create_upside_down_pyramid(5))
