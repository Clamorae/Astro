with open("./Astro/S10/E03","r") as f:
    lines = f.readlines()

sum = 0
for line in lines:
    if line !="#":
        splitted = line.split()
        if splitted[0] != "#":
            sum += int(splitted[1]) * int(splitted[2])

print(sum)