sum=0
top =2
down =9
minus=1

for i in range(3):
    sum_of_serie =top/down
    sum+=sum_of_serie*minus
    top+=3
    down+=4
    minus*=-1
    
print("sum_of_serie=",sum)