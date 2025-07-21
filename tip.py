def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    #erase '$' from the input
    d = d.replace("$","")

    #return the value as a float
    return float(d)


def percent_to_float(p):
    #remove '%' from the input
    p = p.replace("%", "")

    #return the value as a float
    result = float(p) / 100
    return result

main()
