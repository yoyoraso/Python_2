max=0
lst=[1,2,3,2,3,2]
min=lst[0]
for i in range(len(lst)):
    if(lst[i]>max):
        max=lst[i]
    elif(lst[i]<min):
        min=lst[i]

print("max=",max,"Min=",min)