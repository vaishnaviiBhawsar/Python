print("====== WELCOME TO FOOD ORDERING SYSTEM ======")

total_bill = 0

while True:

    print("\n========== FOOD MENU ==========")
    print("1 → Pizza       ₹250")
    print("2 → Burger      ₹120")
    print("3 → Pasta       ₹180")
    print("4 → Sandwich    ₹100")
    print("5 → Cold Drink  ₹50")
    print("6 → Generate Bill & Exit")

    choice = int(input("\nEnter your choice: "))

    match choice:

        case 1:
            qty = int(input("Enter Pizza Quantity: "))
            bill = qty * 250
            total_bill = total_bill + bill
            print("Pizza Added")
            print("Amount =", bill)

        case 2:
            qty = int(input("Enter Burger Quantity: "))
            bill = qty * 120
            total_bill = total_bill + bill
            print("Burger Added")
            print("Amount =", bill)

        case 3:
            qty = int(input("Enter Pasta Quantity: "))
            bill = qty * 180
            total_bill = total_bill + bill
            print("Pasta Added")
            print("Amount =", bill)

        case 4:
            qty = int(input("Enter Sandwich Quantity: "))
            bill = qty * 100
            total_bill = total_bill + bill
            print("Sandwich Added")
            print("Amount =", bill)

        case 5:
            qty = int(input("Enter Cold Drink Quantity: "))
            bill = qty * 50
            total_bill = total_bill + bill
            print("Cold Drink Added")
            print("Amount =", bill)

        case 6:

            print("\n========== FINAL BILL ==========")

            print("Total Bill =", total_bill)

            if total_bill >= 1000:
                discount = total_bill * 10 / 100
                print("Discount =", discount)
                total_bill = total_bill - discount

            else:
                print("No Discount Applied")

            gst = total_bill * 5 / 100
            print("GST =", gst)

            final_amount = total_bill + gst

            print("Final Amount =", final_amount)

            print("\nThanks For Ordering")
            break

        case _:
            print("Invalid Choice")