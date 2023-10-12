import telebot
from telebot import types
from datetime import datetime
from Graf import load_schedule, get_schedule_for_user

bot = telebot.TeleBot('')
days_mapping, datetime_to_df_day_mapping, employee_schedule = load_schedule()

user_answers = {}

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    item_name = types.KeyboardButton('Ввести Фамилию')
    markup.add(item_name)

    Usname = f'<b>Привет {message.from_user.first_name}! Я помогаю сотрудникам с их расписанием, можете выбрать нужный раздел!</b>'
    bot.send_message(message.chat.id, Usname, parse_mode='html', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Ввести Фамилию')
def ask_for_surname(message):
    bot.send_message(message.chat.id, 'Пожалуйста, введите свою фамилию:')
    bot.register_next_step_handler(message, process_surname_step)

def process_surname_step(message):
    surname = message.text
    user_answers[message.from_user.id] = {'surname': surname}

    today_datetime = datetime.today()
    user_schedule_info = get_schedule_for_user(surname, today_datetime, datetime_to_df_day_mapping, days_mapping, employee_schedule)
    bot.send_message(message.chat.id, user_schedule_info)

if __name__ == '__main__':
    bot.polling(none_stop=True)