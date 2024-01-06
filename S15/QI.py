sum = 0

for i in range(1,2*10**6,4):
    sum = sum + 1/i - 1/(i+2)

print(sum*4)