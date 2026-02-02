while True:
    while True:
        try:
            bill_amount = float(input("Enter bill amount: "))
        except ValueError:
            print("Invalid input. Bill amount must be a number. Please try again.")
            continue
        if bill_amount > 0:
            break
        print("Invalid input. Bill amount must be a number > 0. Please try again.")

    while True:
        try:
            tip_percent = float(input("Enter tip (%): "))
        except ValueError:
            print("Invalid input. Tip percent must be a number. Please try again.")
            continue
        if tip_percent >= 0:
            break
        print("Invalid input. Tip percent must be a number >= 0. Please try again.")

    while True:
        try:
            people_count = int(input("Enter number of people: "))
        except ValueError:
            print("Invalid input. Number of people must be an integer. Please try again.")
            continue
        if people_count >= 1:
            break
        print("Invalid input. Number of people must be an integer greater than or equal to 1. Please try again.")

    tip = bill_amount * (tip_percent / 100)
    total = bill_amount + tip
    amount_per_person = total / people_count
    print("Bill amount:", bill_amount)
    print("Tip:", tip)
    print("Total:", total)
    print("Number of people:", people_count)
    print("Amount per person:", amount_per_person)
    again = input("\nCalculate again? (yes/no): ").lower()
    if again == "no":
        break
        
