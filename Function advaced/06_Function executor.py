def func_executor(*args):
    results = []
    for function_name, arguments in args:
        results.append(function_name(*arguments))

    return results



def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))