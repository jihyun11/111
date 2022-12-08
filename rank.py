tot = [60, 0, 70, 60, 70, 80, 100, 60, 80, 100]
rank = [0] * 101
rank_tot = 0
for i in range (len(tot)) :
    rank_tot += rank [tot[i]] + 1
    rank[i] = len(tot) - rank_tot + 1

for i in range (len(tot)) :
    print(i+1, "번째 학생 점수는", tot[i], "석차는", rank[tot[i]])
