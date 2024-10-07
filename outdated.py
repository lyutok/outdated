import re

mothes = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():

    while True:
        user_date = input("Date: ")
        if "/" in user_date:
            date_splited = user_date.split("/")

            try:
                if 0 < int(date_splited[0]) <= 12 and 0 < int(date_splited[1]) <= 31:
                    print(f"{int(date_splited[2])}-{int(date_splited[0]):02}-{int(date_splited[1]):02}")
                    break
            except ValueError:
                pass

        else:
            if "," in user_date:
                date_splited = re.split(',| ', user_date)

                try:
                    i = mothes.index(date_splited[0].capitalize()) + 1
                except ValueError:
                    pass
                else:
                    if 0 < int(date_splited[1]) <= 31:
                        print(f"{date_splited[3]}-{i:02}-{int(date_splited[1]):02}")
                        break


main()

# 9/8/1636 or September 8, 1636
# ['September', '8', '', '1636']
