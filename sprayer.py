import time

import config
config.init()

import db_com
import multitimer

def spray_timer():
    spray_finish.start()
    spray_timeout.start()

def end_spray():
    while(config.humid < config.humid_limit) and (config.spraying==True):
        pass
    if(config.spraying==True):
        db_com.update_db(config.temp, config.humid, 1)
        print("Spraying finished")
        config.spraying = False
        spray_timeout.stop()

def timeout():
    if(config.spraying==True):
        db_com.update_db(config.temp, config.humid, 1)
        print("Spraying timedout")
        config.spraying = False

def Auto_sprayer():
    if(config.spraying == False):
        db_com.update_db(config.temp, config.humid, 3)
        print("Auto Spraying Started")
        config.spraying = True
        spray_timer()
    Auto_spray.stop()
    Auto_spray.start()

Auto_spray = multitimer.MultiTimer(interval=config.auto_delay, function=Auto_sprayer, count=1, runonstart=False)
spray_finish = multitimer.MultiTimer(interval=config.spray_til, function=end_spray, count=1, runonstart=False)
spray_timeout = multitimer.MultiTimer(interval=config.spray_TIMEOUT, function=timeout, count=1, runonstart=False)

