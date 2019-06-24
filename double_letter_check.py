test_string = input("Test value please: ")
print(test_string)

for i,letter in enumerate(test_string[:-1]):
    if letter.isalpha():
        if letter == test_string[i+1]:
            print("Double letter!")
            break