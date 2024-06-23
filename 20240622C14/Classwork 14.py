sumeven=0
for i in range(0,31):
    if i%2==0:
       sumeven=sumeven+i
       print(i,sumeven)
print(sumeven)


sumthree=0
sumfive=0
for i in range(0,31):
    if i%3==0 and i%5==0:
        continue
    if i%3==0:
       sumthree=sumthree+i
       print(i,sumthree)
    if i%5==0:
        sumfive=sumfive+i
        print(i,sumfive)
print(sumthree)
print(sumfive)

#len returns string length
Cafelist=['coffee', 'sandwhich','donut', 'tea']
for food in Cafelist:
    if len(food)>=5:
        print(food)
i=0
while i<20:
    print(i)
    i=i+1
