'''14. online Course Fee System

An online platform offers courses with fixed fees:

* Programming → ₹5000
* Design → ₹4000
* Marketing → ₹3000
  Discount is applied based on user type:
* Student → 20% discount
* Working Professional → 10% discount
* Others → No discount

Write a Python program to calculate final course fee.

Input:
Enter course category: Programming
Enter user type: Student

Output:
Final Course Fee: ₹4000'''

course=("Enter course category:").lower()
user_type=("Enter user type:")
dynamic discount

if course=="Programming":
 if user_type=="student":
  discount=5000*20//100
 if user_type=="working professional":
  discount=5000*10//100
 else:
  print("No discount")
  print("Final Course Fee:",discount)
   
elif course=="design":
 if user_type=="student":
  discount=(4000*20//100)
 if user_type=="working professional":
  discount=(4000*10//100)
 else:
  print("No discount")
  print("Final Course Fee:",discount)

else:
 if user_type=="student":
  discount=(3000*20//100)
 if user_type=="working professional":
  discount=(3000*10//100)
 else:
  print("No discount")
  print("Final Course Fee:",discount)
   

   
