from django.core.mail import send_mail

def send_confirmation_email(email, code):
    full_link = f'https://hakaton-deeee0082bdc.herokuapp.com/api/v1/account/activate/{code}/'
    send_mail(
        'User activation',
        full_link,
        'abdurahimmahau@gmail.com',
        [email]
    )