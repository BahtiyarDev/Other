from telebot import *


aslan = TeleBot('8283501767:AAHAa0U63N_5OCUatTWUzFpdEK3RVLTFUpE')



@aslan.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    file = open('photo_aslan_start.jpg', 'rb')
    markup.add(types.InlineKeyboardButton(
        "Аккаунт моей бабки", url='https://onlyfans.com'))
    aslan.send_photo(message.chat.id, file,
                     caption="Застрелите мою бабку, ведь я Аслан - самый тупорылый бот на свете🦍", reply_markup=markup)
    file.close()


@aslan.my_chat_member_handler()
def handle_new_chat_member(message):
    new_status = message.new_chat_member.status
    if new_status in ['member', 'administrator']:
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(
            "Аккаунт моей бабки", url='https://onlyfans.com'))
        file = open('photo_aslan_start.jpg', 'rb')
        aslan.send_photo(message.chat.id, file,
                         caption="Застрелите мою бабку, ведь я Аслан - самый тупорылый бот на свете🦍", reply_markup=markup)
        file.close()


@aslan.message_handler()
def chatting(message):
    if 'пошел нахуй' in message.text.lower():
        aslan.reply_to(message, "Привет!😁")

    elif 'привет' in message.text.lower().rstrip() or 'здравствуй' in message.text.lower().rstrip():
        aslan.reply_to(message, "Пошел нахуй сын хуйни🤟")

    elif 'пока' in message.text.lower().rstrip() or 'прощай' in message.text.lower().rstrip():
        aslan.reply_to(message, "Пиздуй давай🤟")

    elif 'аслан' in message.text.lower().rstrip():
        aslan.reply_to(message, "Не еби мне мозг аболтуз🤟")

    elif 'сосал' in message.text.lower().rstrip() or 'сосал?' in message.text.lower().rstrip():
        aslan.reply_to(message, "Само собой, своей бабке👌")

    elif 'брат' in message.text.lower().rstrip() or 'твой брат' in message.text.lower().rstrip() or "джавид" in message.text.lower().rstrip() or "джулюк" in message.text.lower().rstrip() or "джамал" in message.text.lower().rstrip():
        aslan.reply_to(
            message, "Это ебаная грязная тварь, я люблю врываться в его комнату и устраивать жесткую оргию😝🤟")

    elif  message.text.lower().rstrip() in ['ok', "ок"]:
        aslan.reply_to(message, "Полизать тебе лобок?😝🤟")

    elif message.text.lower().rstrip() in 'да':
        aslan.reply_to(message, "Пизда моей старушки?🤟")

    elif "зури" in message.text.lower().rstrip():
        file = open('rizvan.jpg', 'rb')
        aslan.send_photo(message.chat.id, file, caption="Ризван мой любимчик👅",
                         reply_to_message_id=message.message_id)

    elif "хорошо" in message.text.lower().rstrip() or "понятно" in message.text.lower().rstrip() or "ясно" in message.text.lower().rstrip():
        aslan.reply_to(message, "НЕТ")

    elif "пидора ответ" in message.text.lower().rstrip() or "пидра ответ" in message.text.lower().rstrip() or "пидара ответ" in message.text.lower().rstrip():
        aslan.reply_to(message, 'Шлюхи аргумент')

    elif message.text.lower().rstrip() in ["чо","че","чё"]:
        aslan.reply_to(message, 'Возвращайся в свой колхоз😝')

    elif message.text.lower().rstrip() in 'эй':
        aslan.reply_to(message, 'Ты мне?')

    elif "скотина" in message.text.lower().rstrip() or "урод" in message.text.lower().rstrip() or "тварь" in message.text.lower().rstrip():
        aslan.reply_to(message, 'О да!')

    elif "член" in message.text.lower().rstrip() or "хуй" in message.text.lower().rstrip() or "пися" in message.text.lower().rstrip() or "писюн" in message.text.lower().rstrip() or "писька" in message.text.lower().rstrip():
        aslan.reply_to(message, 'Я его себе отгрыз😋')

    elif "пизда" in message.text.lower().rstrip() or "манда" in message.text.lower().rstrip():
        aslan.reply_to(message, 'О да, изюм😜')

    elif "очко" in message.text.lower().rstrip():
        aslan.reply_to(message, 'Моей соседки что ли?')

    elif "нет" in message.text.lower().rstrip():
        aslan.reply_to(message, 'Пидора ответ🤣')

    elif "что" in message.text.lower().rstrip():
        aslan.reply_to(message, 'А тебя это ебать не должно😎')

    elif "сын" in message.text.lower().rstrip():
        aslan.reply_to(message, 'Не тебе судить уебище😎')

    elif "ебать" in message.text.lower().rstrip() or "ебал" in message.text.lower().rstrip() or "ебу" in message.text.lower().rstrip():
        aslan.reply_to(message, 'О нет как страшно😖. Но мне похуй😎')

    elif "бот" in message.text.lower().rstrip():
        aslan.reply_to(message, 'Сам ты бот, лоутаб ебаный😎')




aslan.infinity_polling()
