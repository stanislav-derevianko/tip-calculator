while True:
    while True:
        try:
            bill_amount = float(input("Enter bill amount: "))
        except ValueError:
            print("Please enter a number.")
            continue
        if bill_amount >= 1:
            break
        print("Invalid input. Retry")

    while True:
        try:
            tip_percent = float(input("Enter tip (%): "))
        except ValueError:
            print("Please enter a number.")
            continue
        if tip_percent >= 0:
            break
        print("Invalid input. Retry")

    while True:
        try:
            people_count = int(input("Enter number of people: "))
        except ValueError:
            print("Please enter an integer.")
            continue
        if people_count >= 1:
            break
        print("Invalid input. Retry")
        
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
        

