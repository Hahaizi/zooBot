import telebot
from telebot import types

bot = telebot.TeleBot('6535963650:AAFYp__YA0n_yV_x10G-rEdBFAa7H_HjGgg')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Выбрать питомца')
    markup.row(btn1)
    btn2 = types.KeyboardButton('О боте')
    btn3 = types.KeyboardButton('Поддержка')
    markup.row(btn2, btn3)
    btn4 = types.KeyboardButton('Мой питомец')
    markup.row(btn4)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!🌿 Добро пожаловать в мир заботы о редких и экзотических питомцах! Я здесь, чтобы помочь тебе в уходе за своими уникальными друзьями. Будем вместе создавать комфортное и счастливое окружение для твоих особенных питомцев.', reply_markup=markup)
    bot.register_next_step_handler(message, menu)

@bot.message_handler(func=lambda message: True)
def menu(message):
    markup = types.ReplyKeyboardRemove()
    if message.text == 'Выбрать питомца':
        mark = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Кролик', callback_data='btn1')
        btn2 = types.InlineKeyboardButton('Енот(Скоро)', callback_data='btn2')
        btn3 = types.InlineKeyboardButton('Лис(Скоро)', callback_data='btn3')
        mark.row(btn1, btn2, btn3)
        btn4 = types.InlineKeyboardButton('Дикий кот(Скоро)', callback_data='btn4')
        btn5 = types.InlineKeyboardButton('Белка(Скоро)', callback_data='btn5')
        btn6 = types.InlineKeyboardButton('Сова(Скоро)', callback_data='btn6')
        mark.row(btn4, btn5, btn6)
        btn7 = types.InlineKeyboardButton('Аксолотль(Скоро)', callback_data='btn7')
        btn8 = types.InlineKeyboardButton('Игуана(Скоро)', callback_data='btn8')
        btn9 = types.InlineKeyboardButton('Хамелеон(Скоро)', callback_data='btn9')
        mark.row(btn7, btn8, btn9)
        btn10 = types.InlineKeyboardButton('Геккон(Скоро)', callback_data='btn10')
        btn11 = types.InlineKeyboardButton('Ара(Скоро)', callback_data='btn11')
        btn12 = types.InlineKeyboardButton('Фенек(Скоро)', callback_data='btn12')
        mark.row(btn10, btn11, btn12)
        btn13 = types.InlineKeyboardButton('Змея(Скоро)', callback_data='btn13')
        btn14 = types.InlineKeyboardButton('Лемур(Скоро)', callback_data='btn14')
        btn15 = types.InlineKeyboardButton('Капибара(Скоро)', callback_data='btn15')
        mark.row(btn13, btn14, btn15)
        btn16 = types.InlineKeyboardButton('Мини-пиг(Скоро)', callback_data='btn16')
        btn17 = types.InlineKeyboardButton('Паук(Скоро)', callback_data='btn17')
        btn18 = types.InlineKeyboardButton('Таракан(Скоро)', callback_data='btn18')
        mark.row(btn16, btn17, btn18)
        btn19 = types.InlineKeyboardButton('Краб(Скоро)', callback_data='btn19')
        btn20 = types.InlineKeyboardButton('Скунс(Скоро)', callback_data='btn20')
        btn21 = types.InlineKeyboardButton('Утка(Скоро)', callback_data='btn21')
        mark.row(btn19, btn20, btn21)
        btn22 = types.InlineKeyboardButton('Обезьяна(Скоро)', callback_data='btn22')
        btn23 = types.InlineKeyboardButton('Шиншилла(Скоро)', callback_data='btn23')
        mark.row(btn22, btn23)
        bot.send_message(message.chat.id, 'Выбери питомца, который тебя интересует:', reply_markup=mark)
    elif message.text == 'О боте(Скоро)':
        bot.send_message(message.chat.id, 'about', reply_markup=markup)
    elif message.text == 'Поддержка(Скоро)':
        bot.send_message(message.chat.id, 'donate', reply_markup=markup)
    elif message.text == 'Мой питомец(Скоро)':
        bot.send_message(message.chat.id, 'mypet', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == 'btn1':
        bot.send_message(call.message.chat.id, 'Выберите породу кролика')

bot.polling(non_stop=True)
Я В АХУЕ