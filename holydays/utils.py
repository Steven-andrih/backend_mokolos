from datetime import timedelta

def getHolydayDuration(weekEndOption, startDate, endDate):
    if startDate > endDate:
        return -1  # ou tu lèves une exception

    if weekEndOption:
        # Inclut tous les jours
        total = (endDate - startDate).days + 1
        return total
    else:
        # Exclut les weekends (samedi=5, dimanche=6)
        current_day = startDate
        total = 0
        while current_day <= endDate:
            if current_day.weekday() < 5:  # Lundi à vendredi (0 à 4)
                total += 1
            current_day += timedelta(days=1)
        return total
