"""EX01_cashier."""
a = int(input("Enter a sum: "))
b = a % 50
c = b % 20
d = c % 1063
e = d % 5
print(f'Amount of coins needed: {(a//50) + (b//20) + (c//10) + (d//5) + (e//1)}')
