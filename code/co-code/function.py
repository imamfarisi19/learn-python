def say_hi(name, country, hobby, age, statuses, gender): 
    for i in range(10): 
        print("Hello, I'm " + name + ", I'm from " + country + 
              ", My hobby is " + hobby + "\n, my Age " + str(age) + 
              ", statuses now " + statuses + ", gender " + gender + "\n" ) 
        age = age + 1 

if __name__ == "__main__": 
    say_hi("hikaru", "Japan", "listening music", 18, "happy", "Girl") 
