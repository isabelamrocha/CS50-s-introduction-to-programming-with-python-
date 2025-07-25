def main():
    time = input("What time is it? ")
    result = convert(time)

    if 7.0 <= result <= 8.0:
        print("breakfast time")
    elif 12.0 <= result <= 13.0:
        print("lunch time")
    elif 18.0 <= result <= 19.0:
        print("dinner time")


def convert(time):
    hours, minutes = map(float, time.split(":"))
    minutes = minutes / 60
    return hours + minutes


if __name__ == "__main__":
    main()
