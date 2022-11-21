import time
import _thread as thread

import db_com

import calc_val

import config
config.init()

import sprayer

thread.start_new_thread(calc_val.calc_val, ())

sprayer.Auto_spray.start()




while True:
    pass

