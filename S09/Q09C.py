with open("./Astro/S09/dataQC.txt","r") as f:
    lines = f.readlines()

price = 0
for line in lines:
    splitted = line.split()
    if splitted[0]!="#":
        price+=int(splitted[1])*int(splitted[2])

print(f"The total price is {price}")