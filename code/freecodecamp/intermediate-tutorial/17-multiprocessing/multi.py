from multiprocessing import Pool
#from multiprocessing import Process, Value, Array, Lock 
#from multiprocessing import Queue 
#import time 
#import os 

''' 
def square_numbers(): 
    for i in range(1000): 
        i * i 



def add_100(numbers, lock): 
    for i in range(100): 
        time.sleep(0.01) 
        for i in range(len(numbers)):
            with lock:
                numbers[i] += 1
        #with lock: 
        #lock.acquire() 
        #    number.value += 1 
        #lock.release() 



def square(numbers, queue): 
    for i in numbers: 
        queue.put(i*i) 

def make_negative(numbers, queue): 
    for i in numbers: 
        queue.put(-1*i) 
''' 

def cube(number): 
    return number * number * number 

if __name__ == "__main__":  

    numbers = range(10) 
    pool = Pool() 
    
    # map, apply, join, close 
    result = pool.map(cube, numbers) 
    # pool.apply(cube, numbers[0]) 

    pool.close()
    pool.join()

    print(result) 

    ''' 
    numbers = range(1, 6) 
    q = Queue() 

    p1 = Process(target=square, args=(numbers, q)) 
    p2 = Process(target=make_negative, args=(numbers, q)) 
    
    p1.start() 
    p2.start() 

    p1.join() 
    p2.join() 

    while not q.empty(): 
        print(q.get()) 

    


    lock = Lock() 
    shared_array = Array('d',[0.0, 100.0, 200.0]) 
    print('array at beginning is', shared_array[:])
    # shared_number = Value('i', 0) 
    # print('Number at beginning is', shared_number.value) 

    p1 = Process(target=add_100, args=(shared_array,lock)) 
    p2 = Process(target=add_100, args=(shared_array,lock)) 
    
    #p1 = Process(target=add_100, args=(shared_number,lock)) 
    #p2 = Process(target=add_100, args=(shared_number,lock)) 
    
    p1.start() 
    p2.start() 

    p1.join() 
    p2.join() 

    print('array at end is', shared_array[:])
    # print('number at end is', shared_number.value) 



    processes = [] 
    num_processes = os.cpu_count() 
    # number of CPUs on the machine. Usually a good choise for the number of processes 
    
    # create processes and asign a function for each process 
    for i in range(num_processes): 
        process = Process(target=square_numbers) 
        processes.append(process) 

    # start all processes 
    for process in processes: 
        process.start() 

    # wait for all processes to finish 
    # block the main program untill these processes are finished 
    for process in processes: 
        process.join() 
    '''

