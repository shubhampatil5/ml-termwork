import csv

s = ['%', '%', '%', '%', '%', '%']
g0 = ['?', '?', '?', '?', '?', '?']
t = g0[:]
g = []
readCsv = csv.reader(open('Training_examples.csv'), delimiter=',')
data = []
print("\nThe given training examples are:")
for row in readCsv:
    print(row)
    # if row[len(row) - 1].upper() == "YES":
    data.append(row)
# print("\nThe positive examples are:", data[0:])
# print("The steps of the Find-s algorithm are\n", hypo)
d = len(data[0]) - 1
s = data[0][:d]
for i in range(len(data)):
    if data[i][-1] == 'Y':
        for k in range(d):
            if s[k] != data[i][k]:
                s[k] = '?'
        for i in range(len(g)):
            for j in range(d):
                if g[i][j] != '?' and g[i][j] != s[j]:
                    g.pop(i)
    else:
        for k in range(d):
            if s[k] != '?' and s[k] != data[i][k]:
                t[k] = s[k]
                g.append(t[:])
                t[:] = g0[:]
        for i in range(len(g)):
            for j in range(d):
                if g[i][j] != '?' and g[i][j] != s[j]:
                    g.pop(i)

print("s: ",s)
print("g: ",g)
#
# print("\nThe maximally specific Find-s hypothesis for the given training examples is", hypo);
