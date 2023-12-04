with open("./S12/Q1.txt") as f:
    lines = f.readlines()

store = []
counted = []
for word in lines:
    if word not in counted:
        print(f"the word {word[:-1]} appear in the table {lines.count(word)} times")
        counted.append(word)