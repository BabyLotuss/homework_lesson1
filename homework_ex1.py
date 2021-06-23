duration = int(input('Введите число: '))
minute = 60
hour = 3600
day = 86400

if duration < minute:
    print(duration, 'сек')
elif minute <= duration < hour:
    print(duration // minute, 'мин', duration % minute, 'сек')
elif hour <= duration < day:
    print(duration // hour, 'час', duration % hour // minute, 'мин', duration % minute, 'сек')
elif duration > day:
    print(duration // day, 'дн', duration % day // hour, 'час', duration % hour // minute, 'мин', duration % minute,
          'сек')
