def check_loan_eligibility():
   
    try:
        age = int(input("please enter your age 😊: "))
        if age < 0:
            print("Age cannot be negative. Please enter a valid age.")
            return

        income = float(input("Please enter your annual income (in sh): "))
        if income < 0:
            print("Income cannot be negative. Please enter a valid income.")
            return

    
        if age >= 21 and income >= 21000:
            print("Congratulations   😊! You qualify for a loan.")
        else:
            print("unfortunately, we are unable to offer you a loan at this time 💀.")
    
    except ValueError:
        print("Invalid input. Please enter numeric values for age and income.")

check_loan_eligibility()
