'''
This script compares the time taken to do the same task using a Python list and a Numpy Array.
In both cases, the program creates a data structure that holds an array of 10,000,000 random
numbers between 1 and 7. Each process is clocked to evaluate the time taken. As the script 
will prove, Numpy arrays can run up to 100 times faster than ordinary Python list objects.
'''


import time
import numpy as np
import random

start_time_list = time.time()

list1 = [random.randrange(1,7) for i in range(0,10_000_000)]

print(f"Python List --- Process finished --- {(time.time() - start_time_list)} seconds ---")


start_time_array = time.time()

array1 = np.random.randint(1, 7, 10_000_000)

print(f"Numpy Array --- Process finished --- {(time.time() - start_time_array)} seconds ---")
