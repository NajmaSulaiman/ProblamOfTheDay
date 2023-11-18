l1 = [7, 8, 3, 1, 6, 22, 10, 25, 9, 15, 1]
l2 = [2, 11, 0, 6, 3, 20, 7, 25, 6, 7]

if sum(l1[0:4]) < sum(l2[0:4]):
    p1 = l1[0], l1[1], l1[2].l1[3]
else:
    p1 = l2[0], l2[1],l2[2],l2[3]
#print(p1)    
if sum(l1[5:8]) < sum(l2[4:8]):
    p2 = l1[5], l1[6],l1[7]
else:
    p2 = l2[4], l2[5],l2[6],l2[7]
#print(p2)  
if sum(l1[8:11]) < sum(l2[8:10]):
    p3 = l1[8], l1[9],l1[10]
else:
    p3 = l2[8], l2[9]
#print(p3)
print("the shortest path is :"+str((p1+p2+p3)))
print("sum of the shortest path is :"+str(sum(p1+p2+p3)))
