import re
import datetime


def change_date_format(date):
        convert_date = re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', date)
        return convert_date


date_1 = str(datetime.date.today())
print("Original date in YYY-MM-DD Format: ", date_1)
print("New date in DD-MM-YYYY Format: ", change_date_format(date_1))
