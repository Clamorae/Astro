from sklearn.model_selection import train_test_split
import sklearn.neural_network as nn
import sklearn.inspection as inspect
import numpy as np
import matplotlib.figure as figure
import matplotlib.backends.backend_agg as agg

with open("./S15/main.dat") as f:
    main_lines = f.readlines()
with open("./S15/photo.dat") as f:
    photo_lines = f.readlines()

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
    train_x.append(tr_line[1:3])
    train_y.append(tr_line[-1:])
    test_x.append(te_line[1:3])
    test_y.append(te_line[-1:])


train_x = np.array(train_x)
train_y = np.array(train_y)

label = list(set(train_y.flatten()))
print(label)

classifier = nn.MLPClassifier(max_iter=1000)
classifier.fit(train_x, train_y)

fig = figure.Figure()
canvas = agg.FigureCanvasAgg(fig)
ax = fig.add_subplot(111)

inspect.DecisionBoundaryDisplay.from_estimator(classifier, train_x, response_method='predict', ax=ax, alpha=0.3, cmap='coolwarm')

prediction = classifier.predict(test_x)
# results of classification
for i in range (len (prediction)):
# data
    subclass = prediction[i]
    match subclass:
        case "M":
            ax.plot(test_x[i][0], test_x[i][1], linestyle='None', marker='o', markersize=3, color='darkblue', label='Unknown M')
        case "K":
            ax.plot(test_x[i][0], test_x[i][1], linestyle='None', marker='^', markersize=3, color='darkred', label='Unknown K')
        case "F":
            ax.plot(test_x[i][0], test_x[i][1], linestyle='None', marker='>', markersize=3, color='darkgreen', label='Unknown F')
        case "D":
            ax.plot(test_x[i][0], test_x[i][1], linestyle='None', marker='<', markersize=3, color='gold', label='Unknown D')
        case "G":
            ax.plot(test_x[i][0], test_x[i][1], linestyle='None', marker='v', markersize=3, color='grey', label='Unknown G')
        case "A":
            ax.plot(test_x[i][0], test_x[i][1], linestyle='None', marker='*', markersize=3, color='darkpurple', label='Unknown A')
        case "B":
            ax.plot(test_x[i][0], test_x[i][1], linestyle='None', marker='P', markersize=3, color='deeppink', label='Unknown B')

for item,target in zip(train_x,train_y):
    match target:
        case "M":
            ax.plot(item[0], item[1], linestyle='None', marker='o', markersize=3, color='blue', label='Known M')
        case "K":
            ax.plot(item[0], item[1], linestyle='None', marker='^', markersize=3, color='red', label='Known K')
        case "F":
            ax.plot(item[0], item[1], linestyle='None', marker='>', markersize=3, color='green', label='Known F')
        case "D":
            ax.plot(item[0], item[1], linestyle='None', marker='<', markersize=3, color='yellow', label='Known D')
        case "G":
            ax.plot(item[0], item[1], linestyle='None', marker='v', markersize=3, color='black', label='Known G')
        case "A":
            ax.plot(item[0], item[1], linestyle='None', marker='*', markersize=3, color='purple', label='Known A')
        case "B":
            ax.plot(item[0], item[1], linestyle='None', marker='P', markersize=3, color='pink', label='Known B')
fig.savefig("./S15/fig.png", dpi=100)