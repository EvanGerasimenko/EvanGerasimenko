import pyowm
owm = pyowm.OWM ('92105564edd301e393450045b4457058', language = "ru")


while True:


    place = input ('enter your city: ')

    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(place)

    w = observation.weather

    temp = w.temperature('celsius')["temp"]

    print ("in city of " + place + " is " + w.detailed_status + " right now")
    print ("temperature right now is " + str(temp))

    if temp < 10:
	    print ("it's cold right now, get warm clothes")
    elif temp < 25:
	    print ("normal temperature")
    else:
	    print ("temperature is good for light clothes")
