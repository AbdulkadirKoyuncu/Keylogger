import smtplib
import socket

def send_email(subject, body, to_email):
    from_email = 'Write the address to send the mails'
    password = 'Write the password for the e-mail account'
    body = str(body)
    email_text = f"Subject: {subject}\n\n{body}"
    
    try:
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.ehlo()
        smtp_server.login(from_email, password)
        smtp_server.sendmail(from_email, to_email, email_text)
        print("Email sent!")
        
    except (smtplib.SMTPException, socket.error) as e:
        print("An error occurred while sending an email:", e)
        
    finally:
        smtp_server.quit()