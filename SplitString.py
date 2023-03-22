name = "wait for me"

x = []
w = name.split()
for i in w:
    if len(i) > 1:
        x.append(i[0] + ''.join(sorted(i[1:-1]))[::-1] + i[-1])
    else:
        x.append(i)
print (' '.join(x))
