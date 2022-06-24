print('Welcome to Bailey Bank\n')

balance = 100
pin_code = 0000
tries = 0

cust_no = int(input("Please insert your card and enter your 4 number pin code\n"))

try:
    if cust_no == pin_code:
    withdraw = int(input('Thank you please enter your withdrawal amount\n'))
        if withdraw <= balance:
            print('You have withdrawn £{} please wait for your cash'.format(withdraw))
        else:
            print('Value exceeds your balance, please contact your bank.')

except ValueError:
    print('Sorry, please enter 4 numbers')
except Exception as e:
    print('Sorry. Something went wrong {}'.format(e))

elif cust_no != pin_code:
    while tries <= 1:
        print('Incorrect pin. Please try again.')
        cust_no = int(input("Please insert your card and enter your 4 number pin code\n"))
        tries += 1

    else:
        print('Too many pin attempts. Please contact your bank.')

except ValueError:
    print('Sorry, please enter 4 numbers')
except Exception as e:
    print('Sorry. Something went wrong {}'.format(e))

