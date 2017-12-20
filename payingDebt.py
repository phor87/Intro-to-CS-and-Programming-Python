balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
# Remaining balance: 361.61

'''
Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance) 
'''

for i in range(12):
    minimumMonthlyPayment = monthlyPaymentRate * balance
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    balance = monthlyUnpaidBalance + (monthlyUnpaidBalance * (annualInterestRate/12.0))

    print('month', i, 'balance:', balance)

print('Remaining balance:', round(balance,2))