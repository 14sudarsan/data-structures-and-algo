a = [-1,0,1,2,-1,-4]

array =[]

for i in range(0,len(a)):
    
    hash=[]                        #hash is declared for empty list
    
    for j in range(1,len(a)):
        
        third = -(a[i] + a[j])                #-1+0+k=0 , k=1-0 ,k=1 
                                               
        hash.append(a[j])                     #a[j] that is 0  is add to hash then hash= [0]
        
        if third != a[i] and third !=a[j] and third in hash:             #then check the k(1) in hash(0)  is not,if k == hash then the 
                                                                         
            result = [a[i],a[j] , third]  #this the result
            
            sortedresult = sorted(result)
            

    
    array.append(sortedresult)


final =     list(map(list,set(map(tuple,array)))) 

print(final)  
    
    
    

            
            
            
            