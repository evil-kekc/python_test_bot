from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import buttons
import questions
import os

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=MemoryStorage())


class FSMAdmin(StatesGroup):
    first_question = State()
    second_question = State()
    third_question = State()
    fourth_question = State()
    fifth_question = State()
    sixth_question = State()
    seventh_question = State()
    eighth_question = State()
    ninth_question = State()
    tenth_question = State()
    cancel = State()


users = {}


@dp.callback_query_handler(state=FSMAdmin.first_question)
async def send_question(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id, '')
    await bot.send_message(callback_query.from_user.id, f'{questions.first_question}',
                           reply_markup=buttons.first_question_buttons)
    await callback_query.message.delete()
    await FSMAdmin.second_question.set()


@dp.callback_query_handler(
    lambda callback: callback.data in questions.first_question_answers.keys(), state=FSMAdmin.second_question)
async def first_question(callback_query: types.CallbackQuery, state: FSMContext):
    if callback_query.data == 'current_answer':
        await bot.answer_callback_query(callback_query.id, 'Правильный ответ!', show_alert=True)
        await bot.send_message(callback_query.from_user.id, f'{questions.second_question}',
                               reply_markup=buttons.second_question_buttons)
        await callback_query.message.delete()
        await FSMAdmin.third_question.set()
    else:
        await bot.answer_callback_query(callback_query.id, 'Неверно, попробуй еще раз', show_alert=True)
        await FSMAdmin.second_question.set()


@dp.callback_query_handler(
    lambda callback: callback.data in questions.second_question_answers.keys(), state=FSMAdmin.third_question)
async def first_question(callback_query: types.CallbackQuery, state: FSMContext):
    if callback_query.data == 'current_answer':
        await bot.answer_callback_query(callback_query.id, 'Правильный ответ!', show_alert=True)
        await bot.send_message(callback_query.from_user.id, f'{questions.third_question}',
                               reply_markup=buttons.third_question_buttons)
        await callback_query.message.delete()
        await FSMAdmin.fourth_question.set()
    else:
        await bot.answer_callback_query(callback_query.id, 'Неверно, попробуй еще раз', show_alert=True)
        await FSMAdmin.third_question.set()


@dp.callback_query_handler(
    lambda callback: callback.data in questions.third_question_answers.keys(), state=FSMAdmin.fourth_question)
async def first_question(callback_query: types.CallbackQuery, state: FSMContext):
    if callback_query.data == 'current_answer':
        await bot.answer_callback_query(callback_query.id, 'Правильный ответ!', show_alert=True)
        await bot.send_message(callback_query.from_user.id, f'{questions.fourth_question}',
                               reply_markup=buttons.fourth_question_buttons)
        await callback_query.message.delete()
        await FSMAdmin.fifth_question.set()
    else:
        await bot.answer_callback_query(callback_query.id, 'Неверно, попробуй еще раз', show_alert=True)
        await FSMAdmin.fourth_question.set()


@dp.callback_query_handler(
    lambda callback: callback.data in questions.fourth_question_answers.keys(), state=FSMAdmin.fifth_question)
async def first_question(callback_query: types.CallbackQuery, state: FSMContext):
    if callback_query.data == 'current_answer':
        await bot.answer_callback_query(callback_query.id, 'Правильный ответ!', show_alert=True)
        await bot.send_message(callback_query.from_user.id, f'{questions.fifth_question}',
                               reply_markup=buttons.fifth_question_buttons)
        await callback_query.message.delete()
        await FSMAdmin.sixth_question.set()
    else:
        await bot.answer_callback_query(callback_query.id, 'Неверно, попробуй еще раз', show_alert=True)
        await FSMAdmin.fifth_question.set()


@dp.callback_query_handler(
    lambda callback: callback.data in questions.fifth_question_answers.keys(), state=FSMAdmin.sixth_question)
async def first_question(callback_query: types.CallbackQuery, state: FSMContext):
    if callback_query.data == 'current_answer':
        await bot.answer_callback_query(callback_query.id, 'Правильный ответ!', show_alert=True)
        await bot.send_message(callback_query.from_user.id, f'{questions.sixth_question}',
                               reply_markup=buttons.sixth_question_buttons)
        await callback_query.message.delete()
        await FSMAdmin.seventh_question.set()
    else:
        await bot.answer_callback_query(callback_query.id, 'Неверно, попробуй еще раз', show_alert=True)
        await FSMAdmin.sixth_question.set()


@dp.callback_query_handler(
    lambda callback: callback.data in questions.sixth_question_answers.keys(), state=FSMAdmin.seventh_question)
async def first_question(callback_query: types.CallbackQuery, state: FSMContext):
    if callback_query.data == 'current_answer':
        await bot.answer_callback_query(callback_query.id, 'Правильный ответ! Тест завершен', show_alert=True)
        await callback_query.message.delete()
        await state.finish()
        await bot.send_message(callback_query.from_user.id, 'Выберите действие', reply_markup=buttons.start_buttons)
        await FSMAdmin.first_question.set()
    else:
        await bot.answer_callback_query(callback_query.id, 'Неверно, попробуй еще раз', show_alert=True)
        await FSMAdmin.sixth_question.set()


@dp.callback_query_handler(lambda callback: callback.data == 'cancel_button', state=FSMAdmin.cancel)
async def cancel(callback_query: types.CallbackQuery, state=FSMContext):
    await bot.answer_callback_query(callback_query.id, 'Тест завершен', show_alert=True)
    await callback_query.message.delete()
    await state.finish()
    await bot.send_message(callback_query.from_user.id, 'Выберите действие', reply_markup=buttons.start_buttons)
    await FSMAdmin.first_question.set()


@dp.message_handler()
async def start_mess(message: types.Message, state: FSMContext):
    global users
    await message.answer('Выберите действие',
                         reply_markup=buttons.start_buttons)
    if message.from_user.id not in users.keys():
        users[message.from_user.id] = {}
        users[message.from_user.id]['message.from_user.full_name'] = 0
    await FSMAdmin.first_question.set()


if __name__ == '__main__':
    print('bot polling started')
    executor.start_polling(dp)
