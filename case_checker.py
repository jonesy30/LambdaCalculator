test_string = input("Test value please: ")
print(test_string)

test_list = list(test_string)
for i,letter in enumerate(test_list):
    if letter.isalpha():
        if letter.isupper():
            print("Uppercase letter "+letter)
            test_list[i] = letter.lower()

test_string = "".join(test_list)
print(test_string)