
total_paid = 0

for i in range (1, 13):
    min_month_pay = balance * monthlyPaymentRate
    total_paid += min_month_pay
    balance = balance - min_month_pay
    balance = balance * (1 + annualInterestRate/12)
    print ("Month: "+ str (i))
    print ("Minimum monthly payment: " + str (round (min_month_pay, 2)))
    print ("Remaining balance: " + str (round (balance, 2)))

print ("Total paid : " + str (round (total_paid, 2)))
print ("Remaining balance : " + str (round (balance, 2)))