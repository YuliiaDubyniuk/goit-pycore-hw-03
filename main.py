from datetime import datetime, timedelta, date
import random
import re


"""Task one"""


def get_days_from_today(date: str) -> int:
    """
    Calculate days between current date and provided date.
    Return difference in days as integer.
    """

    date_obj = datetime.strptime(date, "%Y-%m-%d").date()
    current_date = datetime.today().date()

    days_difference = (current_date - date_obj).days

    return days_difference


"""Task two"""


def get_numbers_ticket(min_num: int, max_num: int, quantity: int) -> list:
    """
    Generate list of unique numbers equal given quantity
    in range of the provided min and max values.
    """
    valid_min = min_num >= 1 and min_num < 1000
    valid_max = max_num > min_num and max_num <= 1000
    valid_qty = quantity in range(min_num, max_num + 1)

    if not valid_min or not valid_max:
        print('min_num should be equal or more than 1.\n'
              'max_num should be bigger than min_num and less or equal to 1000.\n'
              f'Your min_num is {min_num} and max_num is {max_num}. Please change invalid values.')
        return []
    elif not valid_qty:
        print('quantity should be in a range of the provided min and max values. Please change quantity.')
        return []
    else:
        generated_numbers = random.sample(
            range(min_num, max_num+1), k=quantity)
        sorted_numbers = sorted(generated_numbers)
        return sorted_numbers


"""Task three"""


def normalize_phone(phone_number: str) -> str:
    """
    Update phone number to follow required standard +38011111111111.
    """
    pattern = r'[^+\d]'
    cleaned_phone = re.sub(pattern, '', phone_number)

    match cleaned_phone:
        case cleaned_phone if cleaned_phone.startswith('+38') and len(cleaned_phone) == 13:
            return cleaned_phone
        case cleaned_phone if cleaned_phone.startswith('38') and len(cleaned_phone) == 12:
            return '+' + cleaned_phone
        case cleaned_phone if cleaned_phone.startswith('0') and len(cleaned_phone) == 10:
            return '+38' + cleaned_phone
        case _:
            print(f"Invalid phone number: {phone_number}.")


"""Task four"""


def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
    """
    Return a list of users with birthdays in the next 7 days with 
    moving greetings date to Monday, if birthday is on weekend.
    """
    current_date = datetime.today().date()
    current_year = current_date.year

    next_week_birthdays = []
    # no information what to do with later future birthdays, so just keep them here
    future_birthday_greeting_dates = []

    for user in users:
        user_dob = datetime.strptime(user['birthday'], '%Y.%m.%d').date()
        user_birthday = user_dob.replace(year=current_year)

        if user_birthday < current_date:
            # user already had a birthday this year
            next_birthday_year = user_birthday.year + 1
            next_birthday = user_birthday.replace(year=next_birthday_year)
            next_year_greeting_day = get_birthday_greeting_date(
                next_birthday).strftime("%Y.%m.%d")
            future_birthday_greeting_dates.append(
                {user['name']: next_year_greeting_day})
        else:
            days_to_birthday = (user_birthday - current_date).days
            greeting_date = get_birthday_greeting_date(
                user_birthday).strftime("%Y.%m.%d")

            if days_to_birthday <= 7:
                # user has a birthday in the next 7 days
                next_week_birthdays.append({user['name']: greeting_date})
            else:
                # user has birthday later this year
                future_birthday_greeting_dates.append(
                    {user['name']: greeting_date})

    return next_week_birthdays


def get_birthday_greeting_date(birthday: date) -> date:
    weekday = birthday.weekday()
    if weekday == 5:  # birthday is on Saturday
        birthday += timedelta(days=2)
    elif weekday == 6:  # birthday is on Sunday
        birthday += timedelta(days=1)
    return birthday
