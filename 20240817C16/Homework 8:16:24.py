myList=[0,1,0,0,0,0,1,0,0,0,]
def filter_myList(myList,filter=None):
    for i in myList:
        if filter == i :
            print(i)

        if filter==None:
            print(i)
        
filter_myList(myList)
filter_myList(myList,0)
filter_myList(myList,1)



