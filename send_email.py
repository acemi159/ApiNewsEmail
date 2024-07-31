import smtplib , ssl


def send_email(email_message, email, password, receiver):
    """
    Send an email using SMTP over SSL.

    Args:
        email_message (str): The message to be sent in the email.
        email (str): The sender's email address.
        password (str): The sender's email password.
        receiver (str): The recipient's email address.

    Returns:
        bool: True if the email was sent successfully, False otherwise.
    """
    if email and password:
        host = "smtp.gmail.com"
        port = 465

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(email, password)
            server.sendmail(email, receiver, email_message)
        return True
    else:
        return False