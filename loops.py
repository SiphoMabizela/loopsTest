def count_items(items):
    # TODO: Return the number of items in the list
    return len(items)

def sum_numbers(numbers):
    # TODO: Return the sum of all numbers in the list
    return sum(numbers)

def find_largest(numbers):
    # TODO: Return the largest number in the list
    return max(numbers)

def count_even_numbers(numbers):
    # TODO: Return the count of even numbers in the list
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count = count +1
    return count


def sum_digits(number):
    # TODO: Return the sum of digits in the given number
    convert_to_string = str(number)
    new_conversion = list(convert_to_string)
    count = 0
    for num in new_conversion:
        count = count + int(num)
    return count

def count_vowels(string):
    # TODO: Return the count of vowels in the string (case-insensitive)
    char = "AEIOUaeiou"
    count = 0
    for letter in string:
        if letter in char:
            count = count +1
    return count

def multiply_list_elements(numbers):
    # TODO: Return the product of all elements in the list
    answer = 1
    for i in numbers:
        answer = answer *i
    return answer