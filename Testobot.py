import telebot
from telebot import types

bot = telebot.TeleBot('7150477853:AAEm521rljp4lPA_CTtJFIaB15fwTu8ZKEs')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помошник!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Телефония')
        btn2 = types.KeyboardButton('Бд')
        btn3 = types.KeyboardButton('Видеонаблюдение')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓ С чем возникла проблема?', reply_markup=markup) #ответ бота


    elif message.text == 'Телефония':
        bot.send_message(message.from_user.id, 'Выключите и включите')
    elif message.text == 'Бд':
        bot.send_message(message.from_user.id, 'Переписывайте заново')

    elif message.text == 'Видеонаблюдение':
        bot.send_message(message.from_user.id, 'Нет проблем, мы всё видим')

bot.polling(none_stop=True, interval=0)