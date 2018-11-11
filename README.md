# Lambda Reminder

A simple [AWS lambda](https://aws.amazon.com/lambda/) application to send periodic reminders via email.

This application sends you a mail on a fixed day/time every week giving a list of people you should call
up to stay in touch. The preset frequency for each person in the csv file 'contact_info.csv' is used to
determine if the person should be contacted this week.

The csv file 'contact_info.csv' contains 3 columns which contain the name of a person, the frequency with which
you wish to contact the person and the date when the entry for the person was made in the table.

## lambda_function.py

This function acts as an entry point for the AWS lambda function. The file 'contact_info.csv' is read row 
by row to determine whether a person is eligible to be contacted in the current week.

## mail_sender.py
Sends a mail to the user from another preconfigured email address by utilizing SMTP mailing.

## validation.py
Determines if a certain person is eligible to contacted this week.

## Setting the schedule
A periodic rule can be created using AWS Lambda that triggers the lambda_function.py at a fixed
period. Info regarding the same can be found [here](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/RunLambdaSchedule.html).

# Requirements
```
os
sys
csv
json
smtplib
datetime
```

