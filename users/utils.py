from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from users.models import User
from holydays.models import Holyday
from permissions.models import Permission

def send_invitation_email(user_email, password_temp):
    subject = "Mail de mise à jour d'information de MOKOLOS "
    from_email = None
    to = [user_email]

    context = {
        'email': user_email,
        'password': password_temp,
        'login_link': 'http://localhost:3000'
    }

    text_content = f"Votre mot de passe temporaire est : {password_temp}"
    html_content = render_to_string("emails/invitation.html", context)

    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()

def send_response_conge_email(user, conge):
    subject = "Mail de retour de demande de congé chez MOKOLOS"
    from_email = None  # email d'envoi configuré, ex: "no-reply@mokolos.com"
    to = [user.email]

    context = {
        'email': user.email,
        'request_date': conge.request_date,
        'start_date': conge.start_date,
        'end_date': conge.end_date,
        'total': conge.total,
        'conge': conge,  
    }

    text_content = f"Votre demande de congé est : {conge.status}"
    html_content = render_to_string("emails/response_demande_conge.html", context)

    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def send_response_permission_email(user, permission):
    subject = "Réponse à votre demande de permission - MOKOLOS"
    from_email = None 
    to = [user.email]

    context = {
        "email": user.email,
        "request_date": permission.request_date,
        "start_date": permission.start_date,
        "end_date": permission.end_date,
        "beginning_hour": permission.beginning_hour,
        "end_time": permission.end_time,
        "nature": permission.nature,
        "status": permission.status,
    }

    text_content = f"Votre demande de permission est : {permission.status}"
    html_content = render_to_string("emails/response_demande_permission.html", context)

    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()

