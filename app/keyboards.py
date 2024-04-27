from aiogram.types import  ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

keyboardReady = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Готов'),
                                          KeyboardButton(text='Не готов')]],
                               resize_keyboard=True,
                               input_field_placeholder="Выберите пункт меню")

keyboardStart = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Начать')]],
                               resize_keyboard=True,
                               input_field_placeholder="Выберите пункт меню")

keyboardDecide = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Следующий вопрос'), KeyboardButton(text='Забрать выигрыш')]],resize_keyboard=True,
                                    input_field_placeholder="Выберите пункт меню")

keyboardAgain = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Снова')], [KeyboardButton(text='Нет')]], one_time_keyboard=True,
                                    resize_keyboard=True,
                                    input_field_placeholder="Выберите пункт меню")



quest0 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='100 кг', callback_data='false')],
                                              [InlineKeyboardButton(text='777 тонн', callback_data='true')],
                                              [InlineKeyboardButton(text='10 кг', callback_data='false')],
                                              [InlineKeyboardButton(text='1 тонну', callback_data='false')]],
                                   resize_keyboard=True,
                                   input_field_placeholder="Выберите пункт меню")

quest1= InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Синий', callback_data='false')],
                                              [InlineKeyboardButton(text='Зеленый', callback_data='false')],
                                              [InlineKeyboardButton(text='Фиолетовый', callback_data='false')],
                                              [InlineKeyboardButton(text='Розовый', callback_data='true')]],
                                   resize_keyboard=True,
                                   input_field_placeholder="Выберите пункт меню")

quest2 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='1', callback_data='false')],
                                              [InlineKeyboardButton(text='2', callback_data='false')],
                                              [InlineKeyboardButton(text='3', callback_data='true')],
                                              [InlineKeyboardButton(text='4', callback_data='false')]],
                                   resize_keyboard=True,
                                   input_field_placeholder="Выберите пункт меню")

quest3 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='♣️', callback_data='true')],
                                              [InlineKeyboardButton(text='/', callback_data='false')],
                                              [InlineKeyboardButton(text='*', callback_data='false')],
                                              [InlineKeyboardButton(text='+', callback_data='false')]],
                                   resize_keyboard=True,
                                   input_field_placeholder="Выберите пункт меню")

quest4 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Гепард', callback_data='false')],
                                              [InlineKeyboardButton(text='Павлин', callback_data='false')],
                                              [InlineKeyboardButton(text='Окунь', callback_data='true')],
                                              [InlineKeyboardButton(text='Еж', callback_data='false')]],
                                   resize_keyboard=True,
                                   input_field_placeholder="Выберите пункт меню")