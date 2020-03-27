list1 = [10, 20, 10, 20, 30, 40, 30, 50]
list2 = [10,20,60,70,80,90,30]
list3 = []
for n in list1:
	if n not in list2:
		list3.append(n)
for n in list2:
	if n not in list1:
		list3.append(n)
print ("list1: ", list1)
print ("list2: ", list2)
print ("list3: ", list3)