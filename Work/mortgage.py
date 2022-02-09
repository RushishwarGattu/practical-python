# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
i=0

while principal > 0:

    
    if i>=61 and i<=108:
        principal = principal * (1+rate/12) - payment-1000
        total_paid = total_paid + payment+1000
    else:
        principal = principal * (1+rate/12) - payment
    
        total_paid = total_paid + payment
    i+=1

    print(i, total_paid,principal)