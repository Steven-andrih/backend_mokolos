from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_invitation_email(user_email, password_temp):
    subject = "Mail de mise à jour d'information de MOKOLOS "
    from_email = None
    to = [user_email]

    context = {
        'email': user_email,
        'password': password_temp,
        'login_link': 'http://localhost:5173/api/login/'
    }

    text_content = f"Votre mot de passe temporaire est : {password_temp}"
    html_content = render_to_string("emails/invitation.html", context)

    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
