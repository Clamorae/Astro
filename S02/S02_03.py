import argparse
import random
import statistics

parser = argparse.ArgumentParser(description = 'adding two integers')
parser.add_argument('n1',type = int,default = 1,help = "mean")
parser.add_argument('n2',type = int,default = 1,help = "Standard Deviation")

args = parser.parse_args()
mean = args.n1
stddev = args.n2

random.seed()

number = []

for i in range(10**6):
    
    number.append(random.gauss( mean , stddev ))

mean = statistics.mean(number)
stddev = statistics.stdev(number)
print(f"mean : {mean}\nstandard deviation : {stddev}")
