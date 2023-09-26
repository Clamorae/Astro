import random
import statistics


random.seed()

mean = 10000
stddev = 300.0
number = []

for i in range(10**6):
    
    number.append(random.gauss( mean , stddev ))

mean = statistics.mean(number)
stddev = statistics.stdev(number)
print(f"mean : {mean}\nstandard deviation : {stddev}")