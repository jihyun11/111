source_array = [2, 1, 9, 3, 5, 6]

list = []

for i in range (len(source_array)) :
        if source_array[i] % 2 == 1:
            list.append(source_array[i])
            list.sort()

