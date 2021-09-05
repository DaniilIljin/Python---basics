"""EX01_cashier."""
entered_ammount_of_money = int(input("Enter a sum: "))
remnant1 = entered_ammount_of_money % 50 # I will find a remnant from each division(50,20,10,5)
remnant2 = remnant1 % 20
remnant3 = remnant2 % 10
remnant4 = remnant3 % 5
# In the answer I will find the integer after each division and sum them up (greedy algorithm)
print(f'Amount of coins needed: {(entered_ammount_of_money//50) + (remnant1//20) + (remnant2//10) + (remnant3//5) + (remnant4//1)}')
