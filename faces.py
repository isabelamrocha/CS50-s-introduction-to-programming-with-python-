#main function
def main():
    #prompts the user for input
    text = input("")
    #calls convert and prints the result
    text = convert(text)
    print(text)

#function that takes a string as input and returns it with a face
def convert(string):
    result = string.replace(":)", "🙂")
    result = result.replace(":(", "🙁")

    return result

main()
