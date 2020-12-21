# function for factorial calculation
def factorial(integer):
    # 0! == 1
    if integer == 0:
        return 1
    else:
        # variable for increment
        multiplier = 1

        # counter
        factorial_counter = 1

        # factorial logic
        while multiplier < integer + 1:
            factorial_counter *= multiplier
            multiplier += 1

        return factorial_counter


# function that converts number to the sum of its digits
def digits_in_number_counter(number: int):
    sum_of_digits = 0
    for digit in str(number):
        sum_of_digits += int(digit)
    return sum_of_digits


# example of usage
print(digits_in_number_counter(factorial(100)))
