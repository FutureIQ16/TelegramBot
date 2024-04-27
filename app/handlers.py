from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

import app.keyboards as kb

router = Router()

money = [0, 5000, 10000, 50000, 100000, 250000]
asks = ['Сколько весит туча в потрясающем мире драконов?', "Какой цвет имеет вкус полыни в сказочной стране Шоколендии?",
        "Сколько ушей у слона в мире параллельной реальности?", "Какой математический символ используется для умножения в детском мультсериале \"Котэ и пёсэ\"?",
        "Какой из этих животных был бы лучшим партнером для танго?"]

ask = 0
WinMoney = 0
button = True
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply('Приветствую тебя в игре "Кто хочет стать миллионером, готов начать игру?',
                        reply_markup=kb.keyboardStart)

@router.message(F.text == 'Начать')
async def game0(message: Message):
    global ask, WinMoney, button
    ask = 0
    WinMoney = 0
    button = True
    await message.reply('Игра будет состоять из 5 вопросов, 4 ответа на каждый, 1 правильный, а также не будет подсказок', reply_markup=kb.keyboardReady)

@router.message(F.text == 'Готов')
async def game1(message: Message):
    await message.reply(f'Вопрос № {ask+1}: {asks[ask]}', reply_markup=kb.quest0)

@router.message(F.text == 'Снова')
async def game0(message: Message):
    global ask, WinMoney, button
    ask = 0
    WinMoney = 0
    button = True
    await message.reply('Вы снова решили сыграть в "Кто хочет стать миллионером", нажимайте на кнопку👇 как будете готовы', reply_markup=kb.keyboardReady)


@router.message(F.text == "Не готов")
async  def NotReady(message: Message):
    await message.answer('Чтож, когда будете готовы жмите на кнопку👇', reply_markup=kb.keyboardStart)

@router.callback_query(F.data == 'true')
async def true(callback: CallbackQuery):
    global ask, WinMoney, button
    await callback.answer()
    if button == False:
        await callback.answer("Вы уже ответили на этот вопрос")
    if ask == 4 and button == True:
        await callback.message.answer(
            f"Совершенно верно! Я Вас поздравляю, Ваш окончательный баланс = {money[WinMoney + 1]} рублей! Вы одержали победу! Хотите сыграть еще раз?",reply_markup=kb.keyboardAgain)
    elif ask < 4 and button == True:
        await callback.message.answer(f"Совершенно верно! Я Вас поздравляю на Вашем балансе теперь {money[WinMoney + 1]} рублей! Для перехода к следующему вопросу - "
                                  "нажмите кнопку \"Следующий вопрос\", если хотите забрать выигрыш - \"Забрать выигрыш\"", reply_markup=kb.keyboardDecide)

    if ask < 5 and button == True:
        ask += 1
        WinMoney += 1
        button = False

@router.message(F.text == 'Следующий вопрос')
async def next(message:Message):
    global button, ask
    button = True
    if ask >= 5:
        await message.reply("Вы ответили на все вопросы")
    elif ask == 1:
        await message.reply(f'Хорошо, вопрос №{ask+1}: {asks[ask]}', reply_markup=kb.quest1)
    elif ask == 2:
        await message.reply(f'Хорошо, вопрос №{ask+1}: {asks[ask]}', reply_markup=kb.quest2)
    elif ask == 3:
        await message.reply(f'Хорошо, вопрос №{ask+1}: {asks[ask]}', reply_markup=kb.quest3)
    else:
        await message.reply(f'Хорошо, вопрос №{ask+1}: {asks[ask]}', reply_markup=kb.quest4)


@router.callback_query(F.data == 'false')
async def false(callback: CallbackQuery):
    global button
    if button == False:
        await callback.answer("Вы уже ответили на этот вопрос")
    else:
        await callback.answer()
        await callback.message.answer("К сожалению, Вы ответили неправильно, баланс Ваш обнуляется, Вы проиграли😩. Хотите попробовать еще?",reply_markup=kb.keyboardAgain)
    button = False

@router.message(F.text == 'Забрать выигрыш')
async def win(message:Message):
    await message.reply(f"Поздавляем с победой😊, Ваш баланс = {money[WinMoney]} рублей 🤑! Хотите сыграть еще раз?",reply_markup=kb.keyboardAgain)

@router.message(F.text == 'Нет')
async def no(message:Message):
    await message.reply(f"Хорошо, {message.from_user.full_name}, ждем Вашего возвращения!🥰🥰🤗", reply_markup=kb.keyboardStart)

