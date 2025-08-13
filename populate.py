# import os
# import django
# import random
# from datetime import datetime, timedelta, date
# from django.utils import timezone

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
# django.setup()

# from users.models import User
# from holydays.models import Holyday

# def random_date(year, month):
#     """Renvoie une date aléatoire dans le mois donné."""
#     day = random.randint(1, 28)  # pour éviter soucis de jours > 28
#     return date(year, month, day)

# def run():
#     users = User.objects.all()
#     statuses = ['pending', 'approved', 'rejected']
#     current_year = datetime.now().year

#     holyday_objects = []

#     for user in users:
#         # Pour chaque mois, créer 1 à 3 congés pour cet user
#         for month in range(1, 13):
#             nb_conges = random.randint(1, 3)
#             for _ in range(nb_conges):
#                 start = random_date(current_year, month)
#                 duration = random.randint(1, 5)  # congé de 1 à 5 jours
#                 end = start + timedelta(days=duration - 1)
#                 status = random.choice(statuses)

#                 holyday = Holyday(
#                     user=user,
#                     start_date=start,
#                     end_date=end,
#                     leave_reasons="Congé annuel",
#                     total=duration,
#                     status=status,
#                     locale='fr',
#                     # request_date sera auto_add
#                 )
#                 holyday_objects.append(holyday)

#     # Insert bulk
#     Holyday.objects.bulk_create(holyday_objects)
#     print(f"{len(holyday_objects)} congés insérés avec succès.")

# if __name__ == '__main__':
#     run()

# Pour les permissions :
import os
import django
import random
from datetime import datetime, timedelta, date, time
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from users.models import User
from permissions.models import Permission  # adapte selon ton app et modèle

def random_date(year, month):
    day = random.randint(1, 28)  # éviter soucis jours > 28
    return date(year, month, day)

def random_time():
    hour = random.randint(8, 18)
    minute = random.choice([0, 15, 30, 45])
    return time(hour=hour, minute=minute)

def run():
    users = User.objects.all()
    statuses = ['pending', 'approved', 'rejected']
    natures = ['Réunion', 'Urgence', 'Consultation', 'Déplacement', 'Affaire personnelle']

    current_year = datetime.now().year
    permission_objects = []

    for user in users:
        for month in range(1, 13):
            nb_perms = random.randint(1, 3)
            for _ in range(nb_perms):
                start_date = random_date(current_year, month)
                end_date = start_date + timedelta(days=random.randint(0, 2))  # permission 1 à 3 jours max

                beginning_hour = datetime.combine(start_date, random_time())
                end_time = datetime.combine(end_date, random_time())

                # S'assurer que end_time >= beginning_hour
                if end_time < beginning_hour:
                    end_time = beginning_hour + timedelta(hours=1)

                # Convertir en aware datetime pour éviter warnings
                beginning_hour = timezone.make_aware(beginning_hour)
                end_time = timezone.make_aware(end_time)

                status = random.choice(statuses)
                nature = random.choice(natures)

                permission = Permission(
                    user=user,
                    start_date=start_date,
                    end_date=end_date,
                    beginning_hour=beginning_hour,
                    end_time=end_time,
                    nature=nature,
                    status=status,
                    locale='fr',
                )
                permission_objects.append(permission)

    Permission.objects.bulk_create(permission_objects)
    print(f"{len(permission_objects)} permissions insérées avec succès.")

if __name__ == '__main__':
    run()
