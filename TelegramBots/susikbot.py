from telebot import *
import webbrowser
import sqlite3

bot = TeleBot('8242501301:AAGL9ua7y0eC4tC5qZMKe8J1J6mVMHY_FbQ')


# @bot.message_handler(commands=['site', 'website'])
# def site(message):
#     webbrowser.open('https://www.wikipedia.org/')


# @bot.message_handler(commands=['start'])
# def main(message):  # message хранит инфу о чате
#     markup = types.ReplyKeyboardMarkup()
#     btn1 = types.KeyboardButton('Удалить фото')
#     btn2 = types.KeyboardButton('Изменить текст')
#     btn3 = types.KeyboardButton('Перейти на сайт')
#     markup.row(btn1)
#     markup.row(btn2, btn3)
#     file = open('photo.jpg', 'rb')
#     # bot.send_message(message.chat.id, "Привет, пупс!", reply_markup=markup)
#     bot.send_photo(message.chat.id, file, caption="Привет пупс! ")
#     bot.register_next_step_handler(message, on_click)


# def on_click(message):
#     if message.text == 'Перейти на сайт':
#         webbrowser.open('https://www.wikipedia.org/')


# @bot.message_handler(content_types=['photo'])
# def work_with_photo(message):
#     markup = types.InlineKeyboardMarkup()
#     btn1 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
#     btn2 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
#     btn3 = types.InlineKeyboardButton(
#         'Перейти на сайт', url='https://www.wikipedia.org/')
#     markup.row(btn1)
#     markup.row(btn2, btn3)
#     bot.reply_to(message, 'Какое красивое фото!', reply_markup=markup)


# @bot.message_handler()
# def user_inp(message):
#     if message.text.lower() in ["привет", 'hello']:
#         bot.send_message(
#             message.chat.id, f'Привет, {message.from_user.first_name}!')
#     elif message.text.lower() == 'id':
#         bot.reply_to(message, f'Ваш ID: {message.from_user.id}')


# @bot.callback_query_handler(func=lambda callback: True)
# def callback_message(callback):
#     if callback.data == 'delete':
#         bot.delete_message(callback.message.chat.id,
#                            callback.message.message_id - 1)
#     elif callback.data == 'edit':
#         bot.edit_message_text(
#             "Edited text", callback.message.chat.id, callback.message.message_id)
        




@bot.message_handler(commands=['db'])
def data_base(message):
    con = sqlite3.connect('database.db')
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                password TEXT)
                
""")
    con.commit()
    cur.close()
    con.close()

    bot.send_message(message.chat.id, "Сейчас тебя зарегистрируем! Введи свое имя: ")
    bot.register_next_step_handler(message, reg_name)

name = ''

def reg_name(message):
    name = message.text.strip()
    bot.send_message(message.chat.id, "Так! Запомнил! Придумай и введи пароль: ")
    bot.register_next_step_handler(message, reg_pass, name)

def reg_pass(message, name):
    password = message.text.strip()

    con = sqlite3.connect('database.db')
    cur = con.cursor()

    cur.execute('INSERT INTO users (name, password) VALUES(?,?)', (name, password))

    con.commit()
    cur.close()
    con.close()

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Вывести всех пользователей", callback_data='users'))
    bot.send_message(message.chat.id, "Регистрация прошла успешно!", reply_markup=markup)

@bot.callback_query_handler(lambda call:True)
def callback(call):
    con = sqlite3.connect('database.db')
    cur = con.cursor()

    cur.execute('SELECT * FROM users')
    users = cur.fetchall()

    info = ''

    for el in users:
        info+= f'Имя: {el[1]}|||Пароль: {el[2]}\n'

    cur.close()
    con.close()

    bot.send_message(call.message.chat.id, f"""Список всех пользователей:
{info}""")




    




# bot.infinity_polling()
bot.polling(non_stop=True)  # Поддерживает бота включенным
