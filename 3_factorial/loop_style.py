digit = 1
factorial_counter = 1
sum_of_factorial_digits = 0

while digit < 101:
    factorial_counter *= digit
    digit += 1

print(factorial_counter)

for i in str(factorial_counter):
    sum_of_factorial_digits += int(i)

print(sum_of_factorial_digits)
