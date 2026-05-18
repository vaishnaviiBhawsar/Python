'''11. Railway Ticket Fare System


A railway system calculates ticket fare based on distance and travel class:

* Distance ≤100 km:
  Sleeper → ₹100, AC → ₹200
* Distance 101–500 km:
  Sleeper → ₹300, AC → ₹600
* Distance >500 km:
  Sleeper → ₹500, AC → ₹1000

Write a Python program to calculate ticket fare.

Input:
Enter distance: 350
Enter class: AC

Output:
Total Fare: ₹600'''

distance=int(input("Enter distance:"))
clss=input("Enter class (AC/Sleeper) : ").lower()

if distance<=100:
  if clss=="sleeper" :
    print("Total fare: 100")
  elif clss=="ac":
    print("Total fare: 200")

elif distance>=101 and distance<=500:
  if clss=="sleeper" :
    print("Total fare: 300")
  elif clss=="ac":
    print("Total fare: 600")
  
else:
  if clss=="sleeper" :
    print("Total fare: 500")
  elif clss=="ac":
    print("Total fare: 1000")

