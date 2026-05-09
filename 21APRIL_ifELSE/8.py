'''8. Smart Farming Irrigation System

A farming system decides irrigation based on soil moisture, temperature, crop type, and rainfall prediction.

If soil moisture is 30 or below, then check temperature. If temperature is at least 35, then check crop type. If wheat, high water supply; otherwise moderate supply. If temperature is less than 35, moderate supply. If moisture is above 30, then check if it is up to 60. If yes, then check rainfall. If rain expected, delay irrigation; otherwise light irrigation. If moisture is above 60, no irrigation.

Input:
Soil Moisture = 25
Temperature = 36
Crop = wheat

Output:
Irrigation = High Water Supply'''

moisture = int(input("Enter Soil Moisture: "))
temperature = int(input("Enter Temperature: "))

if moisture <= 30:
    
    if temperature >= 35:
        crop = input("Enter Crop Type: ").lower()
        
        if crop == "wheat":
            print("Irrigation = High Water Supply")
        else:
            print("Irrigation = Moderate Supply")
    
    else:
        print("Irrigation = Moderate Supply")

elif moisture <= 60:
    rain = input("Is Rain Expected? (yes/no): ").lower()
    
    if rain == "yes":
        print("Irrigation = Delay Irrigation")
    else:
        print("Irrigation = Light Irrigation")

else:
    print("Irrigation = No Irrigation")
