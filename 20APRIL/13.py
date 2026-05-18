'''13. Employee Performance Appraisal System


A company evaluates employees based on performance rating (1–5):

* 5 → 25% salary hike
* 4 → 20% salary hike
* 3 → 10% salary hike
* 2 → 5% salary hike
* 1 → No hike
  If salary is below ₹20000 and rating is 4 or above, an additional ₹2000 bonus is given.

Write a Python program to calculate revised salary.

Input:
Enter salary: 18000
Enter rating: 4

Output:
Revised Salary: ₹23600'''

salary=int(input("Enter salary: "))
rating=int(input("Enter rating: "))

if rating==5:
 if salary<20000:
  bonus=2000
  final_salary=(salary*25//100)+salary+bonus
  print("Revised Salary:" , final_salary)

elif rating==4:
 if salary<20000:
  bonus=2000
  final_salary=(salary*20//100)+salary+bonus
  print("Revised Salary:" , final_salary)

elif rating==3:
  final_salary=(salary*10//100)+salary
  print("Revised Salary:" , final_salary)

elif rating==2:
  final_salary=(salary*5//100)+salary
  print("Revised Salary:" , final_salary)

else:
 print("No Hike")


