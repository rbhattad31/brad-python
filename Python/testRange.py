List =[1,2,4,76,98,90,4,1922]

x,y=0,2000

res = all(ele >= x and ele < y for ele in List)

print(res)