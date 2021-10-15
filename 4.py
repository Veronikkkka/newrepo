def calculate_expression(expression):
    """
    str -> int
  
    """
    index = expression.find("буде ")
    operation = ""
    first, second = "", ""
    # print(first_num)
    index_space = expression.find(" ", index+5)
    for i in range(index+5, index_space):
        first += expression[i]
    print(first)
    for i in range(index_space+1, expression.find(" ", index_space+1)):
        operation += expression[i]
    print(operation)
    index_space = expression.find(" ", index_space+1)
    if operation == "помножити" or  operation == "поділити":
        index_space = index_space + 3
        # index_space = expression.find(" ", index_space+1)
    second = expression[index_space+1:expression.find(" ", index_space+1)]
    print(second)
calculate_expression("Скільки буде 10 поділити на -2 додати 11 мінус -3?")