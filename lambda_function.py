import csv
import json
from validation import validate_date
from mail_sender import send_mail

FILE_NAME = "contact_info.csv"


def lambda_handler(event, context):
    eligible_persons = []

    with open(FILE_NAME, "r") as f:
        csv_dictreader = csv.DictReader(f)
        for r in csv_dictreader:
            print(r.get("beginning_date"))
            valid = validate_date(r.get("beginning_date"), r.get("Frequency"))
            if valid:
                eligible_persons.append(r.get("Person"))
    print(eligible_persons)

    eligible_persons = ",".join(eligible_persons)
    ret_val = send_mail(eligible_persons)
    status_body = "Successfully sent the mail" if ret_val else "Some shit!"
    return {"statusCode": 200, "body": json.dumps(status_body)}
