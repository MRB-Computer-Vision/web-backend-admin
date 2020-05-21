
def send_email(recipient, body):
  msg = mail.send(
        'Send Mail tutorial!',
        recipients=[recipient],
        body=body
    )
  return 'Mail sent'