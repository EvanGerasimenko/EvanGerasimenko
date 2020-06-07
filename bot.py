import pyowm 
import telebot

owm = pyowm.OWM ('92105564edd301e393450045b4457058')
bot = telebot.TeleBot ("1267015948:AAEoRI1nEOKk5YiszX-VL7oGA3rTxoBpBkg")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place( message.text )

    w = observation.weather

    temp = w.temperature('celsius')["temp"]

    answer = "in city of " + message.text + " is " + w.detailed_status + " right now" + "\n"
    answer += "temperature is " + str(temp) + "\n\n"

    if temp < 10: 
	    answer += ("it's cold right now, get warm clothes")
    elif temp < 25:
	    answer += ("normal temperature")
    else:
	    answer += ("temperature is good for light clothes")    
	
    bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True)