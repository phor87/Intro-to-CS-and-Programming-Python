'''
Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

	      Test Case 3:
	      balance = 3926
	      annualInterestRate = 0.2

	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 360
'''

balance = 3926
annualInterestRate = 0.2

lowestPayment = 0
testBalance = balance
while testBalance > 0:
    testBalance = balance
    lowestPayment += 10
    for i in range(12):
        testBalance = testBalance - lowestPayment
        testBalance = testBalance + ((annualInterestRate / 12) * testBalance)

print('Lowest Payment:', lowestPayment)