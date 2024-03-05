def output(input_str):
    rev_St = ""
    for char in input_str:
        rev_St = char + rev_St
    return rev_St


original_str = input("Enter the string:\n")
palin_str = output(original_str)
print(palin_str)

if original_str == palin_str:
    print("palindrome")
else:
    print("Its not palindrome")

