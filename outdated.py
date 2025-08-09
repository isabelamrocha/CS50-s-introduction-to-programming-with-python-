while True:
    try:
        calendar = ['january',
                    'february',
                    'march',
                    'april',
                    'may',
                    'june',
                    'july',
                    'august',
                    'september',
                    'october',
                    'november',
                    'december',
                    ]
        #prompt the user for date
        date_input = input("Date: ").strip().lower()

        #if date_input in MM/DD/YYYY format
        if '/' in date_input:
            date = date_input.split('/')
            month = int(date[0])
            day = int(date[1])
            year = int(date[2])

        #if date_input in MONTH DAY, YEAR format
        elif ',' in date_input:
            date = date_input.replace(',', '').split()
            month_name = date[0]
            #search for the index of the month in 'calendar' and add 1
            month = calendar.index(month_name) + 1
            day = int(date[1])
            year = int(date[2])

        #if the input is not in any format requested it should raise error
        else:
            raise ValueError

        #check if the date is possible
        if day < 1 or day > 31 or month < 1 or month > 12:
            raise ValueError

        print(f"{year}-{month:02}-{day:02}")
        break
    except (ValueError):
        pass
