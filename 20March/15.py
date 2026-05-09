'''15. Smart Parking System

A smart parking system charges based on vehicle type and parking duration:

* Bike → ₹10/hour
* Car → ₹20/hour
* Bus → ₹50/hour
  If parking duration exceeds 5 hours, an additional ₹100 penalty is applied.

Write a Python program to calculate total parking fee.

Input:
Enter vehicle type: Car
Enter hours parked: 6

Output:
Total Parking Fee: ₹220'''


vehicle = input("Enter vehicle type (bike/car/bus): ").lower()
hours = int(input("Enter hours parked: "))

# Set rate
if vehicle == "bike":
    rate = 10
elif vehicle == "car":
    rate = 20
elif vehicle == "bus":
    rate = 50
else:
    print("Invalid vehicle type")
    exit()

# Calculate fee
total = rate * hours

# Add penalty if hours > 5
if hours > 5:
    total = total + 100

print("Total Parking Fee: ₹", total)
