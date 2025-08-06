import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    valid = False
    length = len(s)

    #checks for punctuation and space
    for char in s:
        if char in string.punctuation or char == " ":
            return False

    #check if the plate has a max of 6 characters and min of 2
    if length < 2 or length > 6:
        return False

    #checks if the plate starts with two letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    #check for numbers in the middle of the plate
    first_number = False
    for i in range (length):
        if s[i].isnumeric():
            if first_number == False:
                first_number = True
                if s[i] == '0':
                    return False
        elif first_number == True:
            return False

    #if the plate checks everything, the function should return true
    return True


main()
