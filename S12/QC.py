with open("./S12/QC.txt","r") as f:
    lines = f.readlines()

sum=0
for line in lines:
    if line[0]!="#":
        splitted = line.split(",")
        sum+= int(splitted[1]*int(splitted[2]))

print(sum)