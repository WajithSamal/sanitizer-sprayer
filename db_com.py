import config
import sprayer
import _thread as thread
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

#cred = credentials.Certificate('D:\Programming\key.json')
#firebase_admin.initialize_app(cred)


if not firebase_admin._apps:
    cred = credentials.Certificate('D:\Programming\key.json')
    default_app = firebase_admin.initialize_app(cred)


db = firestore.client()


def update_db(temperature, humidity, status):
    doc_ref = db.collection(u'device').document(u'D000001')

    doc_ref.set({
        u'temperature': temperature,
        u'humidity': humidity,
        u'status': status,
        u'updated_at': round(time.time()*1000),
    }, merge=True)

    config.pre_humid=humidity
    config.pre_temp=temperature


def on_snapshot(doc_snapshot, changes, read_time):
    for doc in doc_snapshot:
        config.status = (doc.to_dict()).get('status')
        if(config.status == 2 and config.spraying == False):
            update_db(config.temp, config.humid, 3)
            print("Spraying Started")
            config.spraying = True
            sprayer.spray_timer()
        if(config.status == 4 and config.spraying == True):
            update_db(config.temp, config.humid, 1)
            print("Spraying Aborted")
            sprayer.spray_finish.stop()
            sprayer.spray_timeout.stop()
            sprayer.Auto_spray.stop()
            sprayer.Auto_spray.start()
            config.spraying = False

doc_ref = db.collection(u'device').document(u'D000001')
doc_watch = doc_ref.on_snapshot(on_snapshot)
