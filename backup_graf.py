import pandas as pd
from datetime import datetime

def graf():
    df = pd.read_excel('рассписание.xlsx')


    days_mapping = {
        'пн': 'понедельник',
        'вт': 'вторник',
        'ср': 'среда',
        'чт': 'четверг',
        'пт': 'пятница',
        'сб': 'суббота',
        'вс': 'воскресенье'
    }

    datetime_to_df_day_mapping = {
        0: 'пн',
        1: 'вт',
        2: 'ср',
        3: 'чт',
        4: 'пт',
        5: 'сб',
        6: 'вс'
    }

    abbreviation_mapping = {
        'АГАТ': 'Агатинская',
        'ДОМО': 'Домодедовская',
        'ОКР': 'Окружная',
        'ВЫХ': 'Выходной'
    }

    employee_schedule = {}
    for index, row in df.iterrows():
        schedule = {}
        for day, value in row[1:].items():
            if isinstance(value, str):
                for abbrev, full_name in abbreviation_mapping.items():
                    if abbrev in value:
                        value = value.replace(abbrev, full_name)
            schedule[day] = value
        employee_schedule[row['Фамилия']] = schedule

    today_datetime = datetime.today()
    today_day_of_week = today_datetime.weekday()
    today_day_df_format = datetime_to_df_day_mapping[today_day_of_week]

    today_full_name = days_mapping.get(today_day_df_format, None)

    user_surname = ''

    if user_surname in employee_schedule:
        user_schedule = employee_schedule[user_surname]

        print(f'График работы для сотрудника, {user_surname}:')
        for day_abbreviation, schedule in user_schedule.items():
            print(f'{day_abbreviation}: {schedule}')

        if today_full_name and today_full_name in user_schedule:
            print(f'\n({today_full_name}). Сегодня у сотрудника, {user_surname}: {user_schedule[today_full_name]}')
        else:
            print(f'\nДля сотрудника {user_surname} не указан график на сегодня ({today_full_name}).')
    else:
        print(
            f'Сотрудник с фамилией {user_surname} не найден.\n Попробуйте написать фамилию в другом регистре(может у вас в графике стоит ваша фамилия в нижнем регистре), либо же уточняйте рассписание у руководителя')


graf()