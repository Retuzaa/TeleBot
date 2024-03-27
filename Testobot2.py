import telebot
from telebot import types

bot = telebot.TeleBot('7150477853:AAEm521rljp4lPA_CTtJFIaB15fwTu8ZKEs')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Главное меню")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помошник!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == 'Главное меню':
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton('Телефония', callback_data='tel')
        item2 = types.InlineKeyboardButton('Бд', callback_data='bd')
        item3 = types.InlineKeyboardButton('Видеонаблюдение', callback_data='vid')
        markup.add(item1, item2, item3)
        bot.send_message(message.from_user.id, '❓ С чем возникла проблема?', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Я не знаю что на это ответить, нажмите на кнопку с нужным вариантом')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            match call.data:
                case 'menu':
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton('Телефония', callback_data='tel')
                    item2 = types.InlineKeyboardButton('Бд', callback_data='bd')
                    item3 = types.InlineKeyboardButton('Видеонаблюдение', callback_data='vid')
                    markup.add(item1, item2, item3)
                    bot.send_message(call.message.chat.id, '❓ С чем возникла проблема?', reply_markup=markup)
                case 'tel':
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton('Не работает номер', callback_data='t1')
                    item2 = types.InlineKeyboardButton('Ничего не работает', callback_data='t2')
                    item3 = types.InlineKeyboardButton('Назад', callback_data='menu')
                    markup.add(item1, item2, item3)
                    bot.send_message(call.message.chat.id, '❓ С чем возникла проблема телефонии?', reply_markup=markup)
                case 'bd':
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton('Все данные исчезли', callback_data='b1')
                    item2 = types.InlineKeyboardButton('Не редактируются данные', callback_data='b2')
                    item3 = types.InlineKeyboardButton('Назад', callback_data='menu')
                    markup.add(item1, item2, item3)
                    bot.send_message(call.message.chat.id, '❓ С чем возникла проблема бд?', reply_markup=markup)
                case 'vid':
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton('Камеры не работают', callback_data='v1')
                    item2 = types.InlineKeyboardButton('Камеры украли', callback_data='v2')
                    item3 = types.InlineKeyboardButton('Назад', callback_data='menu')
                    markup.add(item1, item2, item3)
                    bot.send_message(call.message.chat.id, '❓ С чем возникла проблема видеонаблюдения?', reply_markup=markup)
                case 't1':
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton('Назад', callback_data='tel')
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, 'Проблема с телефонией: Не работает номер \nОчень жаль', reply_markup=markup)
                case 't2':
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton('Назад', callback_data='tel')
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, 'Проблема с телефонией: Ничего не работает \nУ нас всё работает', reply_markup=markup)
                case 'b1':
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton('Назад', callback_data='bd')
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, 'Проблема с базой данных: Все данные исчезли \nМы уже занимаемся решением возникших проблем, а пока полюбуйтесь на цветочек🌸🌿', reply_markup=markup)
                case 'b2':
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton('Назад', callback_data='bd')
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, 'Проблема с базой данных: Не редактируются данные \nНажмите кнопку "Реадктировать"', reply_markup=markup)
                case 'v1':
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    item1 = types.InlineKeyboardButton('Назад', callback_data='vid')
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, 'Проблема с видеонаблюдением: Камеры не работают \nВключите камеры', reply_markup=markup)
                case 'v2':
                    markup = types.InlineKeyboardMarkup(row_width=1)  
                    item1 = types.InlineKeyboardButton('Назад', callback_data='vid')
                    markup.add(item1)
                    bot.send_message(call.message.chat.id, 'Проблема с видеонаблюдением: Камеры украли \nПосмотрите по камерам где они находятся', reply_markup=markup)
        else:
            bot.send_message(call.message.chat.id, 'Я не знаю что на это ответить, нажмите на кнопку с нужным вариантом')
    except Exception as e:
        print(repr(e))
bot.polling(none_stop=True, interval=0)