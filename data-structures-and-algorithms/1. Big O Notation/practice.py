num_list = [1, 2, 3, 4, 5, 6, 7]
num_list2 = ["Lalu", "Rahul", "Nitish", "Samrat"]

def randomFunction(num_list):
    total = 0
    
    for num1 in num_list2:
        for num2 in num_list:
            print(num1, num2)
            total = total + 1
    return total

print(randomFunction(num_list))