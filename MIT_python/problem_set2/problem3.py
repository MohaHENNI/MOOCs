

low = balance / 12
month_rate = annualInterestRate / 12
high = balance / 12 * (1 + month_rate)**12
Epsilon = 0.01
save = balance
a = 0
while abs (balance) >= Epsilon:
    balance = save
    a = (low + high) / 2
    for i in range (12):
        balance = balance - a
        balance = balance * (1 + month_rate)
    if balance > 0:
        low = a
    else:
        high = a

a = round (a, 2)

print ("Lowest Payment: " + str (a))
        