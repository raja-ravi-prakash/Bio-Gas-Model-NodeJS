from sklearn import tree
import csv
import sys

dates = sys.argv
dates.remove("model/sample.py")


features = []
labels = []
with open('daily.csv', newline='\n') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader)
    for row in reader:
        date = row[0].split("-")
        features.append(date)
        labels.append(row[1])

clf = tree.DecisionTreeClassifier()

clf.fit(features, labels)

print(str(clf.predict([dates])).split("[")[1].split("]")[0].split("'")[1])
# print(clf.predict([dates]))
