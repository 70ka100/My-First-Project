Bubblegum = 202
Toffee = 118
Ice_cream = 2250
Milk_chocolate = 1680
Doughnut = 1075
Pancake = 80
Income = Bubblegum + Toffee + Ice_cream + Milk_chocolate + Doughnut + Pancake
print("Earned amount:")
print("Bubblegum: $", Bubblegum, sep='')
print("Toffee: $", Toffee, sep='')
print("Ice cream: $", Ice_cream, sep='')
print("Milk chocolate: $", Milk_chocolate, sep='')
print("Doughnut: $", Doughnut, sep='')
print("Pancake: $", Pancake, sep='')
print()
print("Income: $", float(Income), sep='')
print("Staff expenses:")
Staff = int(input())
print("Other expenses:")
Other = int(input())
print("Net income: $", Income - (Staff + Other), sep='')
