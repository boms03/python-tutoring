Bankaccount = 100
Cafeaccount = 550
foodlist = ['sandwhich', 'tea', 'coffee', 'cookie', 'lemonade']
price_dict = {"sandwhich":20,"tea":8,"coffee":10,"cookie":5, "lemonade":7}    
orderedlist = []
print('Hello welcome to Yoonha\'s Calming Cafe')

while True:
    i=input()
    if i=='1':
        print('What would you like to order?')
        food=input()
        if food in foodlist:
            
            orderedlist.append(food)
            print("You have ordered " + food)
        else:
            print('Sorry, we don\'t have that here')






            
    elif i=='2':
        print('Bye bye, see you soon')
        break
