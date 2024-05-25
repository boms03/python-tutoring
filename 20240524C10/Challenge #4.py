name='yoonha evieland'
alphabets='yoe'

y= 0
o= 0
e= 0
for alphabet in name:
    if alphabet in alphabets:
        if alphabet=='y':
            y=y+1
        elif alphabet=='o':
            o=o+1
        elif alphabet=='e':
            e=e+1
print(y)
print(o)
print(e)
