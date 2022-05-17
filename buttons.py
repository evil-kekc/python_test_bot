from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton
import questions


start_buttons = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)\
    .add(InlineKeyboardButton(text='Начать тестирование', callback_data='start_button'))


first_question_buttons = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
for callback, answer in questions.first_question_answers.items():
    first_question_buttons.add(InlineKeyboardButton(text=f'{answer}', callback_data=f'{callback}'))
first_question_buttons.add(InlineKeyboardButton(text=f'Завершить тест', callback_data=f'cancel_button'))


second_question_buttons = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
for callback, answer in questions.second_question_answers.items():
    second_question_buttons.add(InlineKeyboardButton(text=f'{answer}', callback_data=f'{callback}'))


third_question_buttons = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
for callback, answer in questions.third_question_answers.items():
    third_question_buttons.add(InlineKeyboardButton(text=f'{answer}', callback_data=f'{callback}'))


fourth_question_buttons = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
for callback, answer in questions.fourth_question_answers.items():
    fourth_question_buttons.add(InlineKeyboardButton(text=f'{answer}', callback_data=f'{callback}'))


fifth_question_buttons = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
for callback, answer in questions.fifth_question_answers.items():
    fifth_question_buttons.add(InlineKeyboardButton(text=f'{answer}', callback_data=f'{callback}'))


sixth_question_buttons = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
for callback, answer in questions.sixth_question_answers.items():
    sixth_question_buttons.add(InlineKeyboardButton(text=f'{answer}', callback_data=f'{callback}'))


seventh_question_buttons = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
for callback, answer in questions.seventh_question_answers.items():
    seventh_question_buttons.add(InlineKeyboardButton(text=f'{answer}', callback_data=f'{callback}'))
