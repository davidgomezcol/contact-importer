import re
import datetime

phone_pattern = r"^[(][+]{0,1}[0-9]{1,2}[)]\s/{0,1}[-\s\/0-9]*$"
name_pattern = r'^[a-zA-Z-\s]*$'
email_pattern = r'[^@]+@[^@]+\.[^@]+'


def validate_phone(phone):
    """Validates that a phone number is valid"""
    x = re.search(phone_pattern, phone)
    if x:
        return phone
    else:
        return None


def validate_name(name):
    x = re.search(name_pattern, name)
    if x:
        return name
    else:
        return None


def validate_date(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        return None
    return date


def validate_email(email):
    x = re.search(email_pattern, email)
    if x:
        return email
    else:
        return None


def card_type(number):
    number = str(number)
    card_franchise = ""
    if len(number) == 15:
        if number[:2] == "34" or number[:2] == "37":
            card_franchise = "American Express"
    if len(number) == 13:
        if number[:1] == "4":
            card_franchise = "Visa"
    if len(number) == 16:
        if number[:4] == "6011":
            card_franchise = "Discover"
        if int(number[:2]) >= 51 and int(number[:2]) <= 55:
            card_franchise = "MasterCard"
        if number[:1] == "4":
            card_franchise = "Visa"
        if number[:4] == "3528" or number[:4] == "3529":
            card_franchise = "JCB"
        if int(number[:3]) >= 353 and int(number[:3]) <= 359:
            card_franchise = "JCB"
    if len(number) == 14:
        if number[:2] == "36":
            card_franchise = "Diners Club"
        if int(number[:3]) >= 300 and int(number[:3]) <= 305:
            card_franchise = "Diners Club"
    return card_franchise
