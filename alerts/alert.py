
import smtplib
from email.message import EmailMessage
from twilio.rest import Client

# Email function (similar to your previous code)
def send_email(subject, body, to_email):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to_email

    user = "projectmiddleware@gmail.com"
    msg['from'] = user
    password = "neoz cina bdkp ceek"  # Use the app password generated for your application

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()
    print("Email sent successfully")

# SMS function using Twilio
def send_sms(body, to_phone):
    twilio_account_sid = "ACd3dee1c89a67206ea65f044669dc1370"
    twilio_auth_token = "f66e793f6283312182628098704f19d1"
    twilio_phone_number = "+16787125241"

    client = Client(twilio_account_sid, twilio_auth_token)

    try:
        message = client.messages.create(
            body=body,
            from_=twilio_phone_number,
            to=to_phone
        )
        print("SMS sent successfully")
    except Exception as e:
        print("SMS could not be sent. Error:", str(e))

if __name__ == '__main__':
    # Set your email and SMS recipients
    email_recipient = "vimukthidulnath@gmail.com"
    sms_recipient = "+94763204215"  # Replace with the recipient's phone number

    # Send email
    send_email("Hey", "Hello world", email_recipient)

    # Send SMS
    send_sms("Hello world", sms_recipient)
