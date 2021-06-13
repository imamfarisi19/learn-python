lucky_numbers = [4, 8, 15, 16, 23, 42] 
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"] 

friends.extend(lucky_numbers) 

friends.append("Creed") 

friends.insert(1, "Kelly") 

friends.remove("Jim") 

#friends.clear() 

friends.pop() 

friends.index("Kevin") 

print(friends) 
print(friends.index("Kevin")) 
print(friends.index("Oscar")) 
#print(friends.index("Miky")) 
print(friends.count("Jim")) 

lucky_numbers.sort() 
print(lucky_numbers) 

lucky_numbers.reverse() 
print(lucky_numbers) 

friends2 = friends.copy()
print(friends2) 

