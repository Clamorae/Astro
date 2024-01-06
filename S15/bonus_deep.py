from sklearn.model_selection import train_test_split
import torch.nn as nn
import torch.optim as optim
import torch
import numpy as np
import matplotlib.backends.backend_agg as agg

with open("./S15/main.dat") as f:
    main_lines = f.readlines()
with open("./S15/photo.dat") as f:
    photo_lines = f.readlines()

EPOCHS = 20

dataset = []
improper = 0
for mline, pline in zip(main_lines,photo_lines):
    msplit = mline.split("|")
    psplit = pline.split("|")

    #r ID, U,B,V,R,I,J,H,K, absolute magnitude,spectral type
    useful = [msplit[0], psplit[8], psplit[9], psplit[10], psplit[11], psplit[12], psplit[13], psplit[14], psplit[15],psplit[25],msplit[27]] 

    data_line = [int(useful[0])]
    try:
        for i in range(1,8):
            data_line.append(float(useful[i])-float(useful[i+1]))
        #data_line = [float(useful[1])-float(useful[2]), float(useful[2])-float(useful[3]), float(useful[3])-float(useful[4]), float(useful[4])-float(useful[5]), float(useful[5])-float(useful[6]),float(useful[6])-float(useful[7]),float(useful[7])-float(useful[8])]
        
        data_line.append(float(useful[-2]))
        data_line.append(useful[-1].strip())
        data_line[-1] = data_line[-1][:1].upper()
        dataset.append(data_line)
    except:
        improper +=1

print(dataset[:1])
print(f"{improper} removed for lacking some data, left {len(dataset)} entry")

train, test = train_test_split(dataset,train_size=0.8,shuffle=True)
print(f"Training dataset_size: {len(train)}, Test dataset_size: {len(test)}")

train_x =[]
train_y = []
test_x = []
test_y = []
for tr_line, te_line in zip(train,test):
    train_x.append(tr_line[1:-1])
    train_y.append(tr_line[-1:])
    test_x.append(te_line[1:-1])
    test_y.append(te_line[-1:])


train_x = np.array(train_x)
train_y = np.array(train_y)

label = ["M","K","F","D","G","A","B","S","O"]
print(label)
print(train_x[:1])

buffer_train = []
for i in range(len(train_y)):
    buffer = [0]*len(label)
    buffer[label.index(train_y[i])] = 1
    buffer_train.append(buffer)
train_y = buffer_train
buffer_train = []
for i in range(len(test_y)):
    buffer = [0]*len(label)
    buffer[label.index(test_y[i][0])] = 1
    buffer_train.append(buffer)
test_y = buffer_train

train_x = torch.tensor(train_x,dtype=torch.float)
train_y = torch.tensor(train_y,dtype=torch.float)
test_x = torch.tensor(test_x,dtype=torch.float)
test_y = torch.tensor(test_y,dtype=torch.float)

class NN(nn.Module):
    def __init__(self, input_size,output_size):
        super(NN, self).__init__()
        self.fc = nn.Linear(input_size, output_size)
        self.drop = nn.Dropout()
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(output_size, output_size)
        self.soft = nn.Softmax(dim=0)
    
    def forward(self, x):
        x = self.fc(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.drop(x)
        x = self.soft(x)
        return x

model = NN(len(train_x[0]),len(label))
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(),lr=0.1)

for epoch in range(EPOCHS):
    sum_acc = 0
    sum_loss = 0
    for item,target in zip(train_x,train_y):
        optimizer.zero_grad()
        output = model(item)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()
        if torch.max(output) == torch.max(target):
            sum_acc += 1
        sum_loss += loss.item()
    print(f"[EPOCH {epoch+1}/{EPOCHS}] Average loss: {sum_loss/len(train_x)}, Accuracy: {sum_acc/len(train_x)}")

    if (epoch+1)%5==0:
        with torch.no_grad():
            sum_acc = 0
            sum_loss = 0
            for item,target in zip(test_x,test_y):
                output = model(item)
                loss = criterion(output, target)
                if torch.max(output) == torch.max(target):
                    sum_acc += 1
                sum_loss += loss.item()
            print(f"[Validation] Average loss: {sum_loss/len(train_x)}, Accuracy: {sum_acc/len(train_x)}")
