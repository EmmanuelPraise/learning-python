def main():
    first_number = int(input('Input first number: '))
    second_number = int(input('Input second number: '))
    if first_number < 1 or second_number < 1 or first_number > 100 or second_number > 100:
        print('Your number should not be 0 or lesser neither should it be greater than 100')
        return 0
    add_numbers = first_number + second_number
    print(f'{first_number} + {second_number} = {add_numbers}')
    subtract_numbers = first_number - second_number
    print(f'{first_number} - {second_number} = {subtract_numbers}')
    multiply_numbers = first_number * second_number
    print(f'{first_number} * {second_number} = {multiply_numbers}')
    divide_numbers = first_number / second_number
    print(f'{first_number} / {second_number} = {divide_numbers}')
    return 0
    
    
main()
