import datetime


def validate_date(in_date, freq):
    freq = int(freq)  # Fixing type for frequency
    format_str = '%d-%m-%Y'  # Desired datetime format
    datetime_obj_in = datetime.datetime.strptime(in_date, format_str)  # Conversion of beginning_date to datetime
    weeks_elapsed = int((datetime.datetime.now() - datetime_obj_in).days / 7)
    print(weeks_elapsed)
    if (weeks_elapsed % freq == 0):  # and (weeks_elapsed!=0)): Uncomment if testing successful
        valid = 1
    else:
        valid = 0
    return valid
