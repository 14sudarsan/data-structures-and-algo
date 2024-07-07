a= [1,2,2,3,3,4,5,6]
b=[2,3,3,5,6,6,7]

arr = []
visited = [0,0,0,0,0,0,0]

for i in range(0,len(a)):
    
    for j in range(0,len(b)):
        
        if a[i]==b[j] and visited[j] == 0:

            
            arr.append(a[i])
            visited[j] = 1
            break
int= list(set(a) and set(b))
            
print(arr)
print(visited)