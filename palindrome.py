def is_palindrome_number(num):
    original = str(num)
    reversed_num = original[::-1]
    
    if original == reversed_num:
        print(f"{num} is a palindrome number.")
    else:
        print(f"{num} is not a palindrome number.")

# Example usage
number = int(input("Enter a number: "))
is_palindrome_number(number)