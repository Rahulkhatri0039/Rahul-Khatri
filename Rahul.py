def reverse_string(string):
    # Reversing the input string
    reversed_string = string[::-1]
    return reversed_string

def count_vowels(string):
    # Counting the number of vowels in a string
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in string:
        if char.lower() in vowels:
            count += 1
    return count

# Getting input from the user
input_string = input("Enter a string: ")

# Reversing the input string
reversed_input = reverse_string(input_string)
print("Reversed string:", reversed_input)

# Reversing the reversed string using a loop
reversed_reversed_string = reverse_string(reversed_input)
print("Reversed reversed string:", reversed_reversed_string)

# Counting the number of vowels in the reversed reversed string
vowel_count = count_vowels(reversed_reversed_string)
print("Number of vowels in the reversed reversed string:",vowel_count)