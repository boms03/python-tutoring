Bankaccount = 100
Cafeaccount = 550
foodlist = ['sandwhich', 'tea', 'coffee', 'cookie', 'lemonade']
price_dict = {"sandwhich":20,"tea":8,"coffee":10,"cookie":5, "lemonade":7}    
orderedlist = []
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
            if Bankaccount>=price_dict[food]:
                orderedlist.append(food)
                Bankaccount= Bankaccount-price_dict[food]
                Cafeaccount= Cafeaccount+price_dict[food]
                print("You have ordered " + food)
                
            else:
                print('I\'m sorry but you don\'t have enough') 
        else:
            print('Sorry, we don\'t have that here')
    elif i=='2':
        print('How much tip would you like to give?')
        tip=int(input())
        if Bankaccount>=tip:
            print('You gave ' + str(tip))
            Bankaccount=Bankaccount-tip
            Cafeaccount=Cafeaccount+tip
        orderedlist.clear()
        print('Thank you for coming')
        break
    elif i=='3':
        print('Bye bye, see you soon')
        break
