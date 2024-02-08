age_person = int(input())

days = [365, 30, 1]
unit = ['ano(s)', 'mes(es)', 'dia(s)']

for day in range(len(days)):
    days_life = age_person // days[day]
    
    age_person %= days[day]
    
    print(days_life, unit[day])