import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

soru2 = input("choose language/dili seçiniz(türkçe/english): ").lower().strip()

if soru2 == "türkçe":
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    email = "fakemailer212@gmail.com"
    passw = "vqwiozniobxglwfg"

    server.login(email, passw)

    kime = input("kime atacan: ")
    konu = input("konu ne olacak: ")
    gonderme = input("ne yazacan: ")

    mail = MIMEMultipart()
    mail.attach(MIMEText(gonderme))
    mail['From'] = email
    mail['To'] = kime
    mail['Subject'] = konu
    server.sendmail(email, kime, mail.as_string())
    server.quit()
    print("mesajınız başarıyla işleme alınmıştır✅")
    print("apex tarafından yapılmıştır")

elif soru2 == "english":
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    email = "fakemailer212@gmail.com"
    passw = "vqwiozniobxglwfg"

    server.login(email, passw)

    kime = input("To: ")
    konu = input("Subject: ")
    gonderme = input("Message: ")

    mail = MIMEMultipart()
    mail.attach(MIMEText(gonderme))
    mail['From'] = email
    mail['To'] = kime
    mail['Subject'] = konu
    server.sendmail(email, kime, mail.as_string())
    server.quit()
    print("Your message has been successfully processed.✅")
    print("created by apex")

else:
    print("Geçersiz dil seçimi! / Invalid language choice!")