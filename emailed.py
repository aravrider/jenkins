
import smtplib

my_mail = "aravrider3@gmail.com"
passcode = "hibjljyoybtatmuz"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_mail, password=passcode)

subject = "Trip on this weekend"
body = "Hey, aao kbhi haweli pe"

mail_content = f"Subject: {subject}\n\n{body}"

try:
    connection.sendmail(from_addr=my_mail, to_addrs="amanmahto669@gmail.com", msg=mail_content)
    print("Email sent successfully!")

except Exception as e:
    print("Something went wrong:", e)

connection.close()
