#prompt the user for text
text = input("Input: ")
output =""
#iterate through the text
for char in text:
    if char.lower() in ('a','e','i','o','u'):
        char = ""
    else:
        output += char
print("Output: " + output)
