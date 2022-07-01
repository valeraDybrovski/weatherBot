import telebot
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config

owm = OWM('a109e8d04334904149499684af32bf3e')
mgr = owm.weather_manager()
config_dict = get_default_config()
config_dict['language'] = 'ru'

bot = telebot.TeleBot("5449338576:AAGUD6MM08Pz_TlXPazcIu6pr0RfkERrLsI", parse_mode=None)

@bot.message_handler(content_types=['text'])
def send_echo(message):
	try:
		place = message.text
		observation = mgr.weather_at_place(place)
		w = observation.weather
		temp = w.temperature ('celsius')['temp']
		answer = "В городе " + place+ " сейчас " + w.detailed_status + "\n"
		answer += "Tемпература в этом городе около " + str(temp) + "\n\n"
		if temp <= 10:
			answer +="На улице холодно. Тебе следует одеться по теплее."
		elif temp <= 20:
			answer +="На улице прохладно. Но свитерок всё таки надень."
		elif temp <= 60:
			answer +="На улице ЖАРА. Спокойно можешь идти в шортах."
			bot.send_message(message.chat.id, answer)
	except:
		bot.send_message(message.chat.id, "Назавание города написано неверно. \n" "Или его нет в базе данных.\n")
	#place = message.text
	#observation = mgr.weather_at_place(place)
	#w = observation.weather
	#temp = w.temperature ('celsius')['temp']
	#answer = "В городе " + place+ " сейчас " + w.detailed_status + "\n"
	#answer += "Tемпература в этом городе около " + str(temp) + "\n\n"
	#if temp <= 10:
	#    answer +="На улице холодно. Тебе следует одеться по теплее."
	#elif temp <= 20:
	#    answer +="На улице прохладно. Но свитерок всё таки надень."
	#elif temp <= 60:
	#    answer +="На улице ЖАРА. Спокойно можешь идти в шортах."
#
	#bot.send_message(message.chat.id, answer)

bot.infinity_polling(none_stop = True)