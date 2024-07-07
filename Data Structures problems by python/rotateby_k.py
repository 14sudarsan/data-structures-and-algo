d= int(input("enter thhe number"))

arr=[1,2,3,4,5,6,7]


a=len(arr)%d  #3

temp = arr[0:d]

for i in range(0,len(temp)):
    
    temp[i] = arr[a-i]

print(temp)

temp2 = arr[d:]

print(temp2)

for j in range(1,len(temp2)+1):
    
    print(j)
    
    temp2[j - 1] = temp2[len(temp2) -j]
    
    print(temp2)

    
    

