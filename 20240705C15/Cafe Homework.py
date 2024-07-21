def subtractMoney(Bankaccount,price,number):
    return(Bankaccount-price*number)
def addMoney(Cafeaccount,price,number):
    return(Cafeaccount+price*number)
def addOrder(orderedlist,food,number):
    return(orderedlist+food*number)
Bankaccount = 100
Cafeaccount = 550
foodlist = ['sandwhich', 'tea', 'coffee', 'cookie', 'lemonade']
price_dict = {"sandwhich":20,"tea":8,"coffee":10,"cookie":5, "lemonade":7}
couponlist = [5,10, 15]
orderedlist=def addOrder(orderedlist,food,number)
print('Hello welcome to Yoonha\'s Calming Cafe')
while True:
    print('Current Bankaccount is ' + str(Bankaccount))
    print('Current Cafeacccount is ' + str(Cafeaccount))
    print('Current orderedlist is ' + str(orderedlist))
    i=input()
    
    
    if i=='1':
        print('What would you like to order?')
        food=input()
        if food in foodlist:
            print('How many would you like to order?')
            number=int(input())
            if Bankaccount>=price_dict[food]*number:
                for i in range(number):
                    orderedlist.append(food)
                    Bankaccount=def subtractMoney(Bankaccount,price,number)
                    Cafeaccount=def addMoney(Cafeaccount,price,number)
                    print("You have ordered " + str(number) +' '+ food)

                
            else:
                print('I\'m sorry but you don\'t have enough') 
        else:
            print('Sorry, we don\'t have that here')



    elif i=='2':
        print('How much would you like to use?')
        number=int(input())
        if number in couponlist:
            Bankaccount=Bankaccount+number
            Cafeaccount=Cafeaccount-number
    elif i=='3':
        print('How much tip would you like to give?')
        tip=int(input())
        if Bankaccount>=tip:
            Bankaccount=Bankaccount-tip
            Cafeaccount=Cafeaccount+tip
            print('You gave ' + str(tip))
            orderedlist.clear()
            print('Thank you for coming')
            break
    
    elif i=='4':
        print('Bye bye, see you soon')
        break
