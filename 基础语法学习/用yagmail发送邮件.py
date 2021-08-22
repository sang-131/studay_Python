# import yagmail

# yag = yagmail.SMTP(user='mailnotifier@126.com', password='nicai?', host='smtp.126.com', port='25')
# body = "老师，你好！这是最近工作的文件，请查收。"
# yag.send(to='aochuan103@126.com', subject='工作文件', contents=[body, 'imag.png', 'test.pdf'])
# print("已发送邮件")

import csv

with open("contacts_file.csv") as file:
    reader = csv.reader(file)
    next(reader)    # Skip header row
    for name, email, grade in reader:
        print(f"Sending email to {name}")
        # Send email here