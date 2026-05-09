'''1. Smart Shopping Mall Discount System
A shopping mall offers discounts based on customer type and purchase amount.
If the customer is premium, they get 20% discount when the amount is more than 5000, otherwise 10%.
If the customer is regular, they get 10% discount when the amount is more than 3000, otherwise 5%.
Write a program to calculate the final payable amount using inline if only.'''


type=input("Enter customer type (Premium/Regular)")
amount = int(input("Enter purchase amount:"))
   
discount = (amount * 20) // 100 if type=="premium" and amount>5000 else (amount * 10) // 100  if amount<5000 else (amount * 10) // 100 if type=="regular" and amount>3000 else (amount * 5) // 100
final=amount-discount
print("Final Payable Amount =",final)



'''if type =="premium":
    if amount>5000:
        discount = (amount * 20) // 100
        final = amount-discount
    else:
        discount = (amount * 10) // 100
        final = amount-discount
else:
    if amount>3000:
        discount = (amount * 10) // 100
    else:
        discount = (amount * 5) // 100

print("Final amount =",final)'''
   

