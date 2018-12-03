import csv

s = ['%', '%', '%', '%', '%', '%']
readCsv = csv.reader(open('Training_examples.csv'), delimiter=',')
data = []
print("\nThe given training examples are:")
for row in readCsv:
    print(row)
    if row[-1].upper() == "YES":
        data.append(row)
print("\nThe positive examples are:", data)
print("The steps of the Find-s algorithm are\n", s)
d = len(data[0]) - 1
s = data[0][:d]
for i in range(len(data)):
    for k in range(d):
        if s[k] != data[i][k]:
            s[k] = '?'
    print(s)
print("\nThe maximally specific Find-s hypothesis for the given training examples is", s);
