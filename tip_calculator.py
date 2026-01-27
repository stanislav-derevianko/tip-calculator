while True:
    bill_amount = float(input("enter_bill_amount:"))
    if bill_amount >= 1:
        print(bill_amount)
    else:
        print("Invalid input. Retry")
        continue
    tip_percent = float(input("Enter tip (%):"))
    if tip_percent >= 1:
        print(tip_percent)
    else:
        print("Invalid input. Retry")
        continue
    people_count = int(input("Enter number of people:"))
    if people_count >=1:
        print(people_count)
    else:
        print("Invalid input. Retry")
    tip = bill_amount * (tip_percent / 100)
    total = bill_amount + tip
    amount_per_person = total / people_count
    print("Bill amount:", bill_amount)
    print("Tip:", tip)
    print("Total:", total)
    print("Number of people:", people_count)
    print("Amount per person:", amount_per_person)
    while True:
        again = input("Calculat again: yes/no").lower()
        if again == "no":
            break

