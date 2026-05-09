'''3. Employee Bonus Distribution System
A company provides bonuses based on years of experience.
Experience >10 years → 30% bonus
Experience >5 years → 20% bonus
Otherwise → 10% bonus
Write a program to calculate the total salary after adding bonus using inline if.'''


exp=int(input("Enter experience in years ="))
salary=int(input("Enter salary ="))

bonus=(salary*30)//100 if exp>=10 else (salary*20)//100 if exp>=5 else (salary*10)//100 
total = salary+bonus
print("Total salary =" ,total)