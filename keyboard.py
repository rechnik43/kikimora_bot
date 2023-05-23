#buttons

from telebot import types

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
SearchButton = types.KeyboardButton('показать путевую информацию на сегодня')
markup.add(SearchButton)

markup_choice = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
weather_button = types.KeyboardButton('прогноз погоды')
old_bulletin_button = types.KeyboardButton('показать вчерашний бюллетень')
#buttons = [types.InlineKeyboardButton('показать вчерашний бюллетень'), types.InlineKeyboardButton('прогноз погоды')]
markup_choice.add(SearchButton, weather_button, old_bulletin_button)


#markup_choice = types.InlineKeyboardMarkup(row_width=2)
#weather_button = types.InlineKeyboardButton('прогноз погоды')
#old_bulletin_button = types.InlineKeyboardButton('показать вчерашний бюллетень')
#buttons = [types.InlineKeyboardButton('показать вчерашний бюллетень'), types.InlineKeyboardButton('прогноз погоды')]
#markup_choice.add(weather_button, old_bulletin_button)