import time

resturant_name='ShyEats'
head='shayan'
new_customer='new'
menu='menu'
stats='all good!'

#menu
appetizers = ['Crackers', 'Flatbread', 'Toast']
main_foods = ['Butter Chicken', 'Channa', 'Burgers', 'Big Breakfast']
dessert = ['Ice Cream', 'Chocolat/Strawberry/Caramel Sundae']
bevrages = ['Water', 'Cofee', 'Hot Chocloate']

print('Welcome to this '+ resturant_name +' \n we serve high quality virtual food.\n')
print('Please note that this is a work in progress, my makers a working to make this a better and more quality expirience\n')
time.sleep(3)
name = raw_input('Can I please have your good name to get started(write new if you are a new customer): ')
while name != 'exit':
    if name == head:
        thing = (raw_input('Welcome head what can I do for you?: '))
        if thing == 'stats':
            print('Loading...')
            time.sleep(2)    
            print('Getting configuration codes...')
            time.sleep(3)
            print('Getting Money stats...')
            time.sleep(3)
            print('Getting Likeness stats...')
            time.sleep(5)
            print('Fetching corp. license...')
            time.sleep(12)
            print('Checking certificate validity...')
            time.sleep(9.3)
            print(stats)
            time.sleep(3)

        if thing == 'network':
            print('Fetching network status...')
            time.sleep(5)
            print('Network name: Shahper_4G-plus')
            time.sleep(3)
            print('rest is all good')
            time.sleep(3)
            print('Fetching other stats...')
            time.sleep(12)
            print('Latency: 156 mbps')
            time.sleep(5)

        if thing == 'further updates':
            print('Fetching further updates form staff network...')
            time.sleep(4)
            print('Further updates. \n To be finished around the end of July')
            time.sleep(2)
            print('Menu')
            time.sleep(2)
            print('No name order')
            time.sleep(2)
            print('Party of: tables')
            time.sleep(2)
            print('And much more we haven\'t thought of')
            time.sleep(2)


    if name == new_customer:
        new_question = raw_input('Hello, new customer would you like to set your name (y/n): ')

        if new_question == 'y':
            name1 = raw_input('Your name: ')
            time.sleep(2)
            print('Adding name...')
            time.sleep(5)
            new_name = name1
            print('Your name in the server is now '+ new_name)
            time.sleep(1)
            print('Welcome '+ new_name +' !')
            party_of = raw_input('How may people: ')

            if party_of > 8:
                print('Too many people.. Please go to another resturaunt')
                
            menu = raw_input('Should I show the menu? (y/n): ')

            if menu == 'y':
                print('Apptetizers will be shown first')
                print(appetizers)
                time.sleep(8)
                print('Next main meal')
                print(main_foods)
                time.sleep(8)
                print('Dessert')
                print(dessert)
                time.sleep(8)
                print('Bevrages')
                print(bevrages)
                order0 = raw_input('Do you want to have the price or give the order?: ')

                if order0 == 'price':
                    print('Getting price from server...')
                    time.sleep(2)
                    print('They are all free')
                    time.sleep(1)

                else:
                    order01 = raw_input('May I have your order. Separate them with commas: ')
                    order01ans = order01
                    print('Submitting order...')
                    time.sleep(3)
                    print('Done! \n 2 min. before serving')
                    print('Your order is '+ order01ans)
                    print('Here is a breif summary of your visit till now\n party of: '+ party_of +' nmae: '+ name1 +' order '+ order01ans)
                    time.sleep(5)
                    print('cooking...')
                    time.sleep(60)
                    print('Preparing to serve...')
                    time.sleep(60)
                    print('Dinner served! To eat imagine eating your order')
                    time.sleep(3)
                    payment = raw_input('Please enter your card number: ')
                    time.sleep(1)
                    print('Authenticating...')
                    time.sleep(4)
                    print('Done!')
                    time.sleep(3)
                    print('Thank you for visiting '+ resturaunt_name +' please visit again')
                    
                    
            else:
                print('You can tip us @ tipus.gov.sh')
                time.sleep(5)
        else:
            print('You need to give us your name in order to get going!')
            time.sleep(8)
    elif name == '/exit':
        print('Turnig off...')
        time.sleep(3)
        print('Bye bye')

else:
     print('Not an option. try again')
