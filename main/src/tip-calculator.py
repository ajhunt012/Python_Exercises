bill = float(input("What is your total bill?\n"))

split = float(input("how many people are splitting the bill?\n"))

tip = float (input("Enter the tip percentage that you would like to add.\n"))

tip_percent = (tip * 0.01)
total_tip = bill * tip_percent
total = bill + total_tip
bill_per_person = total/split
final_amount = round(bill_per_person, 2)
print( f"The total for each person should be: ${final_amount}")
