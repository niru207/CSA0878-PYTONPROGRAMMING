s=input("enter the string:")
t=input("enter the string:")
map1=[]
map2=[]
for i in s:
    map1.append(s.index(i))
for j in t:
    map2.append(t.index(j))
if map1==map2:
    print("True \nIt is Isomorphic")
else:
    print("False \nIt is not isomorphic")
            
