# This is KIKIMORA_bot.
# Powered by Salov


import config
import telebot
import requests
from bs4 import BeautifulSoup
import datetime
from keyboard import markup_choice
from keyboard import markup

bot = telebot.TeleBot(config.token)
bot.remove_webhook()


@bot.message_handler(commands=['start'])
def start_message(message):

    bot.send_message(message.chat.id, 'Здравствуйте, я предоставлю путевую информацию от ФГБУ Канал имени Москвы',
                     parse_mode='html', reply_markup=markup)


def way_info(message):
    url = 'https://kim-online.ru/page/navigatsiya/ezhesutochnaya-putevaya-informatsiya/ezhesutochnaya-putevaya-informatsiya-za-2023-god/5016-maj-2023'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    #            bullet = soup.findAll('div', class_="item-text marbot40")
    bullet = soup.find('div', class_="item-text marbot40").find_all('a')
    current_date = datetime.datetime.now().strftime("%d.%m.%Y")
    was_find = False
    for i in bullet:
        if str(i).find(current_date) > -1:
            answer = i.get('href')
            was_find = True
            bot.send_message(message.from_user.id, 'https://kim-online.ru' + answer)
    if was_find == False:
        bot.send_message(message.chat.id,
                         'ФГБУ Канал имени Москвы ещё не опубликовал путевую информацию на сегодня, вы можете воспользоваться вчерашним бюллетенем, или повторить запрос позже. Так же можно посмотреть прогноз погоды')


def weather_info(message):
    URL = 'https://rp5.ru/%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0_%D0%B2_%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B5_(%D0%92%D0%94%D0%9D%D0%A5)'
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup)
    item = soup.findAll('div', class_='round-5')
    # print(item)
    #            item[0].text.strip()
    bot.send_message(message.from_user.id, item[0].text.strip())


def old_bulletin(message):
    url = 'https://kim-online.ru/page/navigatsiya/ezhesutochnaya-putevaya-informatsiya/ezhesutochnaya-putevaya-informatsiya-za-2023-god/5016-maj-2023'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    bullet_old = soup.find('div', class_="item-text marbot40").find_all('a')
    old_date = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%d.%m.%Y")
    for i in bullet_old:
        if str(i).find(old_date) > -1:
            answer = i.get('href')
            bot.send_message(message.from_user.id, 'https://kim-online.ru' + answer)


@bot.message_handler(content_types=['text'])
def bulletin_search(message):
    if message.chat.type == 'private':
        if message.text == 'показать путевую информацию на сегодня':
            way_info(message)
        elif message.text == 'прогноз погоды':
            weather_info(message)
        elif message.text == 'показать вчерашний бюллетень':
            old_bulletin(message)

    bot.send_message(message.chat.id, 'что-то ещё хотите посмотреть?', parse_mode='html', reply_markup=markup_choice)

bot.polling(none_stop=True)

