list = [5, 4, 1, 7, 2]
min = list[0]
for n in list:
    if min > n :
        min = n
list.remove(min)
sec_min = list[0]
for i in list:
    if sec_min > i:
        sec_min = i
print(sec_min)