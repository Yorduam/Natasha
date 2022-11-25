import telebot;
import random;
from telebot import types;

#Токен бота
bot = telebot.TeleBot('5930698074:AAEeCaCjnF2nkOY5saSezt5E3dQOk6xqoto');

print("Бот запущен. Bruh")

name = '';
surname = '';
age = 0;

#Метод на получение сообщений
@bot.message_handler(content_types=['text'])

def help_pannel(message):
    if message.text == '/help':
        bot.send_message(message.from_user.id, 'На данный момент, я знаю:')
        keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
        key_reg = types.InlineKeyboardButton(text='Опросник /reg', callback_data='/reg'); #кнопка «/reg»
        keyboard.add(key_reg);  #добавляем кнопку в клавиатуру
        key_info = types.InlineKeyboardButton(text='Информация обо мне /info', callback_data='/info'); #кнопка «/reg»
        keyboard.add(key_info);  #добавляем кнопку в клавиатуру

#Получение имени
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут?");
        bot.register_next_step_handler(message, get_name);
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg');

def info(message):
    if message.text == '/info':
        bot.send_message(message.from_user.id, "Меня зовут Наташа. Я Telegram-бот, написанный на Python. Моя нынешняя версия 0.0.1. Мне ещё многому учиться.");

#Получение фамилии (наследуемая с start)
def get_name(message):
    global name;
    name = message.text;
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?');
    bot.register_next_step_handler(message, get_surname);

#Получение возраста (наследуемая с name)
def get_surname(message):
    global surname;
    surname = message.text;
    bot.send_message(message.from_user.id, 'Сколько тебе лет?');
    bot.register_next_step_handler(message, get_age);

#Проверка на возраст (наследуемая с surname)
def get_age(message):
    global age;
    while age == 0:
        try:
            age = int(message.text) #Проверяем, что возраст введен корректно
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
    keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes'); #кнопка «Да»
    keyboard.add(key_yes);  #добавляем кнопку в клавиатуру
    key_no= types.InlineKeyboardButton(text='Нет', callback_data='no'); #кнопка «Нет»
    keyboard.add(key_no);   #добавляем кнопку в клавиатуру
    question = 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?';
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

#Реакции на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes": #call.data это callback_data, которую мы указали при объявлении кнопки
        ... #код сохранения данных, или их обработки
        bot.send_message(call.message.chat.id, 'Запомню:)');
    elif call.data == "no":
         ... #переспрашиваем

def starter(call):
    if call.data == "/info":
        info()
    if call.data == "/reg":
        start()
    
bot.polling(none_stop=True, interval=0)

print('Конец программы')