import matplotlib.pyplot as plt
import numpy as np
import csv

epochs = []
evalScore = []
valScore = []
with open('/home/z/Dropbox/bachelorarbeit/Simplenet_Webcam_Line_Detection/epochslog.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        epochs.append(float(row[0]))
        evalScore.append(float(row[1]))
        valScore.append(float(row[2]))

plt.plot(epochs,evalScore)
plt.plot(epochs,valScore)
plt.xlabel('Epochs')
plt.ylabel('Evaluation / Validation score')
plt.title('Evaluation run: Simplenet_4x10')
plt.grid(True)

plt.savefig("test.png")
plt.show()