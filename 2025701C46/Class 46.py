'''Fizzlist=["FizzBuzz" if i%15==0 else "fizz" if i%3==0 else "buzz" if i%5==0 else "nothing"for i in range(1,21)]
print(Fizzlist)
'''


list1=[1,2,3,4,5,6]
list2=[4,5,6,7,8,9]

'''summer={i for i in list1 if i in list2}
print(summer)

summer={i for i in list1 if i not in list2}
print(summer)

summer={i for i in list1+list2 if (i in list1 and i not in list2) or (i in list2 and i not in list1)}
print(summer)'''

summer= {i for i in list1+list2 if i not in {j for j in list1 if j in list2}}
print(summer)
