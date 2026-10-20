ATM = print('Welcome to the ATM. Choose from 4 options and input the serial number in the input box. 1) Check Balance 2) Deposit Amount 3) Withdraw Money 4) Exit')
balance = 5000
choice = int(input('Enter the serial number here: '))
if choice==1:
    print('Your balance is',balance,'Rupees')
elif choice==2:
    deposit = int(input('Enter the deposit here: '))
    nbalance = balance + deposit
    print('The deposit is',deposit,'and the new balance is',nbalance,'Rupees')
elif choice==3:
    withdraw = int(input('Enter the withdrawal here'))
    nbalance = balance-withdraw
    if nbalance<=0:
        print('Unsuccessful Transaction! Amount is less')
    else:
        print('The withdrawal is',withdraw,'and the new balance is',nbalance)
elif choice==4:
    print('Thank you for your services!')
if choice==1 or choice==2 or choice==3:
    print('Welcome to the ATM. Choose from 4 options and input the serial number in the input box. 1) Check Balance 2) Deposit Amount 3) Withdraw Money 4) Exit')
    choice = int(input('Enter the serial number here:'))
elif choice!=1 and choice!=2 and choice!=3 and choice!=4:
    print('Invalid operation!')

