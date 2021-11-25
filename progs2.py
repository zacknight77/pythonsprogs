L1 = [1,3,4,5,6,7,8,10]
print("Given list : ",L1)
res = [x for x in range(L1[0],L1[-1]+1)
       if x not in L1]
print("Missing elements from the list : \n" ,res)

