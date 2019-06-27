"""
Handlers for all commands
"""
from telegram.ext import (CommandHandler,
                          MessageHandler,
                          Filters,
                          RegexHandler,
                          ConversationHandler,
                          CallbackQueryHandler,)

from telegram import (ReplyKeyboardMarkup,
                      KeyboardButton,
                      InlineKeyboardButton,
                      InlineKeyboardMarkup)

from questions import QUIZ_QUESTIONS as Q

import telegram

COUNTER = {}

#KEYBOARDS
MAIN_MENU_MARKUP = ReplyKeyboardMarkup([['Преимущества'],
                                        ['Специальности'],
                                        ['Пройти тест'],
                                        ['Контакты','Соцсети','Адрес'],
                                        ],
                                       resize_keyboard=True)

SOCIAL = InlineKeyboardMarkup(
    [[InlineKeyboardButton("Facebook", url='https://www.facebook.com/kafedra.piitu')],
     [InlineKeyboardButton("Instagram", url='https://www.instagram.com/kafedra_piitu/')],
     [InlineKeyboardButton("Youtube", url='https://www.youtube.com/channel/UCc9ig08a4WFyBRbzIkoAEew')],
     ])

#CONSTANT
INITIAL_MESSAGE = 'Вас приветсвует кафедра *ПИИТУ НТУ "ХПИ"*, выберите интересующий вас пункт меню:'

LOCATION = 'г. Харьков, ул.Кирпичева, 2,корпус У2, 7 этаж.'

CONTACT = 'Телефон: 066-713-79-28, 057-707-69-21\n' \
          'E-mail: vstup.piitu@gmail.com'

ADVANTAGES = '<b>Конкурентные преимущества КАФЕДРЫ ПИИТУ:</b>\n' \
             '<a href="https://piitu-asu.kh.ua/ru.html#liderstvo">1. Обучение на английском языке</a>\n' \
             '<a href="https://piitu-asu.kh.ua/ru.html#diplom">2. Двойные дипломы с университетами Швеции, Австрии, Словакии</a>\n' \
             '<a href="https://piitu-asu.kh.ua/ru.html#liderstvo">3. Проектный подход к образованию, обучение в Innovation Campus</a>\n' \
             '<a href="https://piitu-asu.kh.ua/ru.html#liderstvo">4. Дуальная система обучения</a>\n' \
             '<a href="https://piitu-asu.kh.ua/ru.html#project">5. Мобильность и стажировки студентов в университетах и ИТ-компаниях Украины , Европы, США</a>'
SPECIALTY = '<b>Специальность 121:</b>\n' \
            'Конкурсное предложение «Инженерия программного обеспечения».\n' \
            '<b>Специальность 122:</b>\n' \
            'Конкурсное предложение «Компьютерные науки и интеллектуальные системы».\n' \
            '<b>Специальность 126:</b>\n' \
            'Конкурсное предложение «Программное обеспечение информационных систем».'

# USEFUL FUNCTIONS

# Генерирую клаву
def generate_inline(*step):
    # ARGUMENT FOR STEP KEYBOARD
    # NO ARGUMENT FOR EMPTY KEYBOARD
    if step:
        inline_arr = []

        for i in range(len(Q[step[0]]["answers"])):
            inline_arr.append(InlineKeyboardButton(text=str(i + 1), callback_data=str(step[0])+"."+str(i + 1)))

        inline = InlineKeyboardMarkup([inline_arr])

    else:
        inline = InlineKeyboardMarkup([[]])

    return inline


# Генерирую текст ответа для теста
# если передаю на каком мы сейчас шаге - беру текст из вопросника, нет - можно дописать что угодно
def generate_text(*step):
    if step:
        text = Q[step[0]]["question"]+"\n"

        itr = 1
        for i in Q[step[0]]["answers"]:
            text += str(itr) + " - " + i["text"] + "\n"

            itr += 1
    else:
        text = "Дебаг??"

    return text


# Генерирую результат относительно того какой сейчас шаг и какая кнопка была нажата
def generate_result(*step, result):
    if step:
        result = int(result)-1
        return_result = Q[step[0]-1]["answers"][result]["value"]

    else:
        return_result = "Дебаг??"

    print("return_result: " + str(return_result))
    return return_result


def add_kw(result, chat_id, message_id, **kwargs):
    if not kwargs:
        new_kw = {
            chat_id: {
                message_id: {
                    "result": int(result)
                }
            }
        }
        COUNTER.update(new_kw)
    else:
        new_chat_kw = {
            message_id: {
                "result": int(result)
            }
        }
        COUNTER[chat_id].update(new_chat_kw)


def count_result(message, result):
    # 'message': {'message_id': 436, 'date': 1560638474, 'chat': {'id': 239062390,
    chat_id = message.chat.id
    message_id = message.message_id

    if chat_id not in COUNTER.keys():
        add_kw(result, chat_id, message_id)
    else:
        if message_id not in COUNTER[chat_id]:
            add_kw(result, chat_id, message_id, to_message=True)
        else:
            print("count_result: " + str(COUNTER[chat_id][message_id]["result"]))
            COUNTER[chat_id][message_id]["result"] += int(result)


def delete_query(message):
    chat_id = message.chat.id
    message_id = message.message_id
    if chat_id in COUNTER.keys():
        if message_id in COUNTER[chat_id]:
            COUNTER[chat_id].pop(message_id)
        else:
            if not chat_id:
                COUNTER.pop(chat_id)


def get_result(message):
    # 'message': {'message_id': 436, 'date': 1560638474, 'chat': {'id': 239062390,
    chat_id = message.chat.id
    message_id = message.message_id

    if chat_id in COUNTER.keys():
        if message_id in COUNTER[chat_id].keys():
            return COUNTER[chat_id][message_id]["result"]


# MESSAGE HANDLER
def start(bot, update):
    update.message.reply_text(INITIAL_MESSAGE,
                              reply_markup=MAIN_MENU_MARKUP, parse_mode=telegram.ParseMode.MARKDOWN)


def test_start(bot, update):
    text = generate_text(0)
    markup = generate_inline(0)

    update.message.reply_text(text,
                              reply_markup=markup)

#MENU
def main_menu(bot, update):
    update.message.reply_text('Главное меню',
                              reply_markup=MAIN_MENU_MARKUP)

def advantages(bot, update):
    update.message.reply_text(ADVANTAGES, parse_mode=telegram.ParseMode.HTML)

def specialty(bot, update):
        MARKUP_SPEC = InlineKeyboardMarkup(
            [[InlineKeyboardButton("Подробнее о специальностях", url='https://piitu-asu.kh.ua/ru.html#special')],
             ])
        update.message.reply_text(SPECIALTY, parse_mode=telegram.ParseMode.HTML, reply_markup=MARKUP_SPEC)

def cont(bot, update):
    update.message.reply_text(CONTACT)

def social(bot,update):
    update.message.reply_text('Наши соцсети:', reply_markup=SOCIAL)

def point(bot, update):
    update.message.reply_venue(title='Местоположение', latitude=49.99833297,
                                                       longitude=36.24772668, address=LOCATION)

#MENU
# CALLBACK HANDLER
def callback_handler(bot, update):
    query = update.callback_query

    step, result = query.data.split(".")

    print("Current step: " + step)
    step = int(step) + 1

    if step >= len(Q):
        count_result(query.message, int(generate_result(step, result=result)))
        print("TOTAL RESULT: " + str(get_result(query.message)))

        bot.edit_message_text(chat_id=query.message.chat_id,
                              message_id=query.message.message_id,
                              text="\nВаш результат: " + str(get_result(query.message)),
                              reply_markup=generate_inline())
        bot.answer_callback_query(callback_query_id=query.id, text="Тест завершен")
        delete_query(query.message)

    else:
        count_result(query.message, int(generate_result(step, result=result)))
        bot.edit_message_text(chat_id=query.message.chat_id,
                              message_id=query.message.message_id,
                              text=generate_text(step),
                              reply_markup=generate_inline(step))
        bot.answer_callback_query(callback_query_id=query.id, text="Вы выбрали вариант №" + str(result))



# Handlers for bot
bot_handlers = [CommandHandler('start', start),
                RegexHandler('На главную', main_menu),
                RegexHandler('Преимущества', advantages),
                RegexHandler('Специальности', specialty),
                RegexHandler('Пройти тест', test_start),
                RegexHandler('Соцсети', social),
                RegexHandler('Контакты', cont),
                RegexHandler('Адрес', point),
                CallbackQueryHandler(callback_handler)
                ]


