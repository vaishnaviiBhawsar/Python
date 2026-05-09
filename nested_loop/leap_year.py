'''3)	WAP to find out all the leap years between two entered years'''

y1=int(input("Enter first year"))
y2=int(input("Enter second year"))

print("Leap years are:")

for year in range(y1,y2+1):
      
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
         print(year)

   