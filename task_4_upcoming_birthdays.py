from datetime import datetime, timedelta


def get_upcoming_birthdays(users):

    upcoming_birthdays = []

    today = datetime.today().date()

    for user in users:

        # str to date
        birthday = datetime.strptime(
            user["birthday"],
            "%Y.%m.%d"
        ).date()

        # check if birthday is this year
        birthday_this_year = birthday.replace(year=today.year)

        # if not - postpone to next year
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(
                year=today.year + 1
            )

        # days until birthday
        delta_days = (birthday_this_year - today).days

        # birthdays in next 7 days
        if 0 <= delta_days < 7:

            congratulation_date = birthday_this_year

            # postpone to monday if birthday is on weekend
            if congratulation_date.weekday() >= 5:
                congratulation_date += timedelta(
                    days=7 - congratulation_date.weekday()
                )

            upcoming_birthdays.append(
                {
                    "name": user["name"],
                    "congratulation_date":
                        congratulation_date.strftime("%Y.%m.%d")
                }
            )

    return upcoming_birthdays


users = [
    {"name": "John Doe", "birthday": "1985.05.25"},
    {"name": "Jane Smith", "birthday": "1990.05.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)

print("Список привітань на цьому тижні:")

for user in upcoming_birthdays:
    print(
        f"{user['name']} -> "
        f"{user['congratulation_date']}"
    )