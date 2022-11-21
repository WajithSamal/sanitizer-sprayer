import config
import db_com
#import Adafruit_DHT


def calc_val():
    config.humid = 0
    config.temp = 0



    DHT_SENSOR = Adafruit_DHT.DHT11
    DHT_PIN = 4

"""
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        if humidity is not None and temperature is not None:
            config.humid=humidity
            config.temp=temperature
        if (abs(config.humid-config.pre_humid)>config.humid_threshold) or (abs(config.temp-config.pre_temp)>config.temp_threshold):
            db_com.update_db(config.temp,config.humid,config.status)


"""