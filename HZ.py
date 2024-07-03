num1 = 13.42
num2 = 42.13
def get_integer_part(value): return int(value)
def get_fractional_part(value): return int((value - int(value)) * 100)
integer_part1 = get_integer_part(num1)
integer_part2 = get_integer_part(num2)
fractional_part1 = get_fractional_part(num1)
fractional_part2 = get_fractional_part(num2)
if integer_part1 == fractional_part2 or integer_part2 == fractional_part1:
print("The integer part of one number is equal to the fractional part of the other.")