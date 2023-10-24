age  = int(input("Enter your age\n"))

if age >= 18:
    print('Welcome')
    choix = int(input('Can I offer you something??? 0 or 1\n'))
    if choix == 0:
        print('Ok no probleme')
    else:
        print('Okay wait a minute')
        Drink = int(input('1 FOR WATER 2 FOR SODA 3 FOR BEER\n'))
        if Drink == 1:
            print('Take  your water')
        elif Drink == 2:
            print('Take your soda')
        else:
            print('Take your beer')
else:
    print('Sorry you\'re too young to enter here')

