#prompts the user for the name of a variable in camel case
camel = input("camelCase: ")
#initiates an empty string
snake = ""
#iterate over camel and find the upper case
for letter in camel:
    #if letter is in uppercase it adds "_" and the letter to snake
    if letter.isupper():
        snake += "_" + letter.lower()
    #adds letter to snake
    else:
        snake += letter

#outputs the name is snake case
print("snake_case: " + snake)
