import csv
import smtplib
import configparser

config = configparser.ConfigParser()
config.read('configs.properties')

email_address = config.get('sender_email_details', 'email_address')
email_password = config.get('sender_email_details', 'email_password')

email_server = config.get('email_server_details', 'email_server')
email_port = config.get('email_server_details', 'email_port')


with smtplib.SMTP_SSL(email_server, email_port) as smtp:
    smtp.login(email_address, email_password)

    with open("contacts.csv", 'r') as file1:
        file_data1 = csv.reader(file1, delimiter=',')
        for line in file_data1:
            sender_address = line[0]
            first_name = line[1]
            second_name = line[2]

            subject = "Sample Subject"
            body = """ Hi {0},
                       Please ignore this mail {1}.""".format(first_name, second_name)
            msg = f'Subject:{subject}\n\n{body}'

            smtp.sendmail(email_address, sender_address, msg)

