def is_palindrome(number):
    number_str = str(number)
    if number_str == number_str[::-1]:
        return True
    else:
        return False
my_number = 121
result = is_palindrome(my_number)
if result:
     print(f"Число {my_number} є паліндромом.")
else:
     print(f"Число {my_number} не є паліндромом.")