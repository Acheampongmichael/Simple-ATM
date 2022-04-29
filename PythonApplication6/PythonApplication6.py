print('**************************')
print('Welcome to MA BANK')
print('**************************')
print('Please enter your account number and password below')


while True:
    account_no = input('Account number: ')
    if account_no.isdigit():
        account_no = int(account_no)

    else:
        print('Error, Account number must be in digits')
        continue
    password = input('Password: ')

    if password.isdigit() :
        password = int(password)
        break
    else:
        print('Password must be in digits')
        continue

Acc_Bal = 0

while True:
    print('Choose one option below',"\n",'1 = Deposit',"\n",'2 = Withdraw',"\n",'3 = Account Balance',"\n",'4 =  Exit')
    user_chioice = input()
    user_chioice = int(user_chioice)
    if user_chioice == 1:
        deposit = input('How much do you want to deposit: ')
        deposit = int(deposit)
        Acc_Bal += deposit
        print('CONGRATULATIONS, you made an amount of $', deposit, 'to your account number', account_no )
        print('Account Balance now is $', Acc_Bal,"\n")

    elif user_chioice == 2:
        withdraw = input('How much do you want to withdraw: ')
        withdraw = int(withdraw)
        if withdraw > Acc_Bal:
            print ('Insufficient balance in acount number', account_no,"\n")

        else:
            Acc_Bal -= withdraw
            print('CONGRATULATIONS, you made an amount of $', withdraw, 'from your account number', account_no )
            print('Account Balance now is $', Acc_Bal)

    elif user_chioice == 3:
        print('Account balance in', account_no, 'is $',Acc_Bal)

    elif user_chioice == 4:
        print('Goodbye, Thank you for doing business with us!',"\n")
        break

    else:
        print('Wrong option',"\n")
        continue