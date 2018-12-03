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
    data.append(row)
d = len(data[0]) - 1
s = data[0][:d]
for i in range(len(data)):
    if data[i][-1] == 'Y':
        for j in range(d):
            if s[j] != data[i][j]:
                s[j] = '?'
        for j in range(len(g)):
            for k in range(d):
                if g[j][k] != '?' and g[j][k] != s[k]:
                    g.pop(j)
    else:
        for j in range(d):
            if s[j] != '?' and s[j] != data[i][j]:
                t[j] = s[j]
                g.append(t[:])
                t[:] = g0[:]
        for j in range(len(g)):
            for k in range(d):
                if g[j][k] != '?' and g[j][k] != s[k]:
                    g.pop(i)
    print("s["+str(i)+"]: ",s)
    print("g["+str(i)+"]: ",g)
