'''6. Banking Fraud Detection System

A bank monitors transactions based on amount, location, OTP verification, and account age.

If transaction amount is at least 10000, then check location. If international, then check OTP verification. If verified, allow; otherwise block. If location is domestic, then check if amount is at least 50000. If yes, check account age. If account age is at least 2 years, allow; otherwise flag. If amount is less than 50000, allow. If transaction amount is less than 10000, then check unusual activity. If yes, flag; otherwise allow.

Input:
Transaction Amount = 60000
Location = domestic
Account Age = 1

Output:
Transaction Status = Flagged'''

amount = int(input("Enter Transaction Amount: "))
location = input("Enter Location (domestic/international): ").lower()

if amount >= 10000:
    
    if location == "international":
        otp = input("Is OTP verified? (yes/no): ").lower()
        
        if otp == "yes":
            print("Transaction Status = Allowed")
        else:
            print("Transaction Status = Blocked")
    
    elif location == "domestic":
        
        if amount >= 50000:
            age = int(input("Enter Account Age (years): "))
            
            if age >= 2:
                print("Transaction Status = Allowed")
            else:
                print("Transaction Status = Flagged")
        
        else:
            print("Transaction Status = Allowed")

else:
    unusual = input("Unusual activity detected? (yes/no): ").lower()
    
    if unusual == "yes":
        print("Transaction Status = Flagged")
    else:
        print("Transaction Status = Allowed")

