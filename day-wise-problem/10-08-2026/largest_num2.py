numbers = [30, 10, 20, 50, 40]

largest = numbers[0]

for num in numbers:
    print(num)
    if num  > largest:
        largest = num

print("The largest number of the list: ", largest)