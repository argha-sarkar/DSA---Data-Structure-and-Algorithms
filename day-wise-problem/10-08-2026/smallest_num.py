numbers = [30, 10, 20, 50, 40]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("The smallest number of the list: ", smallest)