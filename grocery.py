#prompt the user for items until the user inputs control-d
grocery_list = {}
i = 0
while True:
    try:
        item = input().upper()
        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1
        i += 1
    except EOFError:
        for item in sorted(grocery_list):
            print(f"{grocery_list[item]} {item}")
        break

#output the user's grocery list in all uppercase
