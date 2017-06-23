r = annualInterestRate / 12

save = balance
a = 0

while balance > 0:
    balance = save
    a += 10
    for i in range (1, 13):
        balance = balance - a
        balance = balance * (1 + r)
    

print ("Lowest Payment: "+ str (a))