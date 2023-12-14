with open("./S13/QF.txt","r") as f:
    lines = f.readlines()

store = []
counted = []
for words in lines:
    for word in words.split():
        if word not in counted:
            store.append(1)
            counted.append(word)
        else:
            store[counted.index(word)]+=1

for i in range(len(counted)):
    print(f"The word {counted[i]} appear {store[i]} times")