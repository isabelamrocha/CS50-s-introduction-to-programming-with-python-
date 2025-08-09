def main():
    #calls for the return_int function with the prompt argument
    fraction = return_int("Fraction: ")

    #output the fuel gauge
    if fraction >= 99:
        print('F')
    elif fraction <= 1:
        print('E')
    else:
        print(fraction, end='')
        print("%")

def return_int(prompt):
    while True:
        try:
            #get input from user and split into two parts (x and y)
            fraction = input(prompt).split('/')

            #transform each part of the input in an int
            x = int(fraction[0])
            y = int(fraction[1])

            #transform the fraction into a percentage and round to the nearest int
            fuel = round((x/y) * 100)

            #force a ValueError if fuel is negative or greater than 100
            if fuel < 0 or fuel > 100:
                raise ValueError

            #return the final value to the main function and break
            return fuel

        #in case of ValuerError or ZeroDivisionError, prompt the user again
        except (ValueError, ZeroDivisionError):
            pass
main()
