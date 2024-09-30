import smtplib
from email.mime.text import MIMEText

def send_email(recipient_email, subject, message):
  """
  Sends an email using the smtplib library.

  **Important:** This is for educational purposes only. Use a secure email API 
  for real-world applications.  Avoid storing email credentials in plain text.

  Args:
      recipient_email: The email address of the recipient.
      subject: The subject line of the email.
      message: The body of the email message.
  """

  sender_email = "<your_email>"  # Replace with your actual email address
  sender_password = "<your_password>"  # Replace with your actual password (not recommended)

  # Create the email message
  email_message = MIMEText(message, 'plain')
  email_message['From'] = sender_email
  email_message['To'] = recipient_email
  email_message['Subject'] = subject

  # Connect to the SMTP server
  with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
      server.login(sender_email, sender_password)
      server.sendmail(sender_email, recipient_email, email_message.as_string())

  print(f"Email sent to {recipient_email} with subject: {subject}")

send_email('recipient@email.com', 'Notification', 'Everything is awesome!')