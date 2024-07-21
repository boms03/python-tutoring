def subtractMoney(Bankaccount,price):
    return(Bankaccount-price)
def addMoney(Cafeaccount,price):
    return(Cafeaccount+price)
Bankaccount = 100
Cafeaccount = 550
foodlist = ['sandwhich', 'tea', 'coffee', 'cookie', 'lemonade']
price_dict = {"sandwhich":20,"tea":8,"coffee":10,"cookie":5, "lemonade":7}
couponlist = [5,10, 15]
orderedlist=[]
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
                price=price_dict[food]*number
                while True: 
                    print('Would you like to use a coupon?')
                    letter=input()
                    if letter == 'y':
                        print('Which one would you like to use?' + str(couponlist))
                        coupon=int(input())
                        if coupon in couponlist:
                            price=price*(100-coupon)/100
                        else:
                            print('I\'m sorry but you don\'t have that coupon')
                        break
                    elif letter =='n':
                        print('Okay, you are not using a coupon')
                        break
                    else:
                        print('please answer with y or n')
                for i in range(number):
                    orderedlist.append(food)
                Bankaccount=subtractMoney(Bankaccount,price)
                Cafeaccount=addMoney(Cafeaccount,price)
                print("You have ordered " + str(number) +' '+ food)
                print('price:'+str(price))
            else:
                print('I\'m sorry but you don\'t have enough') 
        else:
            print('Sorry, we don\'t have that here')



    elif i=='3':
        print('How much tip would you like to give?')
        tip=int(input())
        if Bankaccount>=tip:
            Bankaccount=subtractMoney(Bankaccount,tip)
            Cafeaccount=addMoney(Cafeaccount,tip)
            print('You gave ' + str(tip))
            orderedlist.clear()
            print('Thank you for coming')
            break
    
    elif i=='4':
        print('Bye bye, see you soon')
        break
