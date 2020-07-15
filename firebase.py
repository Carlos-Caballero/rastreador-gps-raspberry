import pyrebase
import time
import firebase_admin
from firebase_admin import credentials

#Credenciales para la comunicación
config = {
    "apiKey": 'AIzaSyDvVTXxBPV-eZ8g_3NW5SLJPZAvjdZcARA',
    'authDomain': 'gps-raspberry-pi-3.firebaseapp.com',
    "databaseURL": 'https://gps-raspberry-pi-3.firebaseio.com',
    "projectId": 'gps-raspberry-pi-3',
    "storageBucket": 'gps-raspberry-pi-3.appspot.com',
    "messagingSenderId": '458926703144',
    "appId": '1:458926703144:web:1fecb7db34d16ed112eb1d',
    "measurementId": 'G-RMB1EG5YEV'
}

#Inicializa la base de datos

firebase = pyrebase.initialize_app(config)
db = firebase.database()
auth = firebase.auth()
#----------------------------------
#--------Código de push------------
#----------------------------------

data = {'latitud' : 'Dato1'}
db.child("database").push(data)
time.sleep(2)                               #retraso de dos segundos
data = {'longitud': 'Dato2'}
db.child("GPS").push(data)
