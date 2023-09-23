# import date class
from datetime import date, timedelta


def get_expiry_date(expires_in: int):
    return date.today() + timedelta(expires_in)
