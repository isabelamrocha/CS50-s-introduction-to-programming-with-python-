#create a variable for the amount due
due = 50
#check if the amount due is bigger than 0
while due > 0:
    #prompt the user to insert coin and update the amount due
    print("Amount Due: " + str(due))
    insert = int(input("Insert Coin: "))
    if insert in (25, 10, 5):
        due -= insert
if due < 0:
    due = -due
print("Change Owed: " + str(due))
