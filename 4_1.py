def calculate_expression(expression):
    """
    str -> int
    """
    numbers_operations = []
    expression = expression[13:]
    numbers_operations = expression.split()
    len_of_arr = len(numbers_operations)
    for i in range(numbers_operations.count("на")):       
        numbers_operations.remove("на")
    numbers_operations[len(numbers_operations)-1] = numbers_operations[len(numbers_operations)-1][:-1]
    print(numbers_operations)
    num = int(numbers_operations[0])    
    for i in range(len_of_arr):
        if i%2 == 0:            
            # try:
            #     numbers_operations[i] = int(numbers_operations[i])
            # except:
            #     return "Неправильний вираз!"
            continue
        elif numbers_operations[i] == "додати" or numbers_operations[i] == "плюс":
            # print(numbers_operations[i+1])
            num += int(numbers_operations[i+1])
        elif numbers_operations[i] == "відняти" or numbers_operations[i] == "мінус":
            num -= int(numbers_operations[i+1])
        elif  numbers_operations[i] == "помножити":
            num *= int(numbers_operations[i+1])
        elif  numbers_operations[i] == "поділити":
            num /= int(numbers_operations[i+1])
        else:
            return "Неправильний вираз!"

        # print(num)
    return int(num)
    # print(expression)
print(calculate_expression("Скільки буде 10 поділити на -2 додати 11 мінус -4?"))