def find_max(arr):
    maximum = arr[0]

    for x in arr:
        if x > maximum:
            maximum = x

    return maximum

print(find_max([10, 12, 8, 15, 6]))