from celery import Task
from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_email_task(email, username):
    '''send_mail(
        'Subject here',
        f'Hello {username}, Here is the message.',
        'from@example.com',
        [email],
        fail_silently=True,
    )'''
    print(username)
    # str = f'Email sent to {str(email)} via celery..'
    return username