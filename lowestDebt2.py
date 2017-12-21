'''
	      Test Case 1:
	      balance = 320000
	      annualInterestRate = 0.2

	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 29157.09
'''
balance = 999999
annualInterestRate = 0.18

lowBound = balance / 12.0
monthlyInterestRate = annualInterestRate / 12.0
upperBound = (balance * (1 + monthlyInterestRate)**12) / 12.0

lowestPayment = (lowBound + upperBound) / 2
testBalance = balance
while testBalance > 0.01:
    for month in range(1,13):
        testBalance = testBalance - lowestPayment
        testBalance = testBalance + ((annualInterestRate / 12) * testBalance)
    if testBalance < 0:
        testBalance = balance
        upperBound = lowestPayment
        lowestPayment = (lowBound + upperBound) / 2
    elif testBalance > 0.01:
        testBalance = balance
        lowBound = lowestPayment
        lowestPayment = (lowBound + upperBound) / 2
print('Lowest Payment:', round(lowestPayment,2))
