import smtplib
from email.message import EmailMessage

def send_email(to_email, voicemail_file):
    msg = EmailMessage()
    msg['Subject'] = "Votre message vocal"
    msg['From'] = "svibot@example.com"
    msg['To'] = to_email
    msg.set_content("Veuillez trouver en pièce jointe votre message vocal.")

    with open(voicemail_file, 'rb') as f:
        msg.add_attachment(f.read(), maintype="audio", subtype="wav", filename="voicemail.wav")

    with smtplib.SMTP('smtp.example.com', 587) as smtp:
        smtp.starttls()
        smtp.login('your_email', 'your_password')
        smtp.send_message(msg)

# Call the function with the necessary parameters
send_email("client@example.com", "/var/spool/asterisk/voicemail/default/6001/INBOX/1234.wav")
