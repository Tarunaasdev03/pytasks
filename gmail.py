import pywhatkit

def sendmail(email_sender, password, subject, message, email_receiver):
    try:
        pywhatkit.send_mail(email_sender, password, subject, message, email_receiver)
        print("Email sent successfully!")
    except Exception as e:
        print("Error:", e)


sendmail ("sender_mail", "Password", "subject", "message", "receiver")
