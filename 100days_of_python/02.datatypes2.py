
age = int(input("What is your current age"))

def calcular_tempo():
    days_today = age * 365
    days_left = (90 * 365) - days_today
    week_today = age * 52
    week_left = (90 * 52) - week_today
    month_today = age * 12
    month_left = (90 * 12) - month_today

    message = f'You have {days_left} days, {week_left} weeks and {month_left} left.'
    print(message)


calcular_tempo()