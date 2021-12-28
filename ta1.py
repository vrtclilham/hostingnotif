from pusher_push_notifications import PushNotifications

import pyrebase
config = {
  'apiKey': "AIzaSyA2g32ThPVN4Eop132xmPlzwKPzI_tYwxc",
  'authDomain' : "ilham-iot.firebaseapp.com",
  'databaseURL' : "https://ilham-iot-default-rtdb.firebaseio.com",
  'projectId' : "ilham-iot",
  'storageBucket' : "ilham-iot.appspot.com",
  'messagingSenderId' : "423724741613"
}

firebase = pyrebase.initialize_app(config)
db=firebase.database()
pn_client = PushNotifications(
instance_id='282b5269-42bd-4740-b141-6bfcd776d979',
secret_key='A3814C0D10D3E13F050905913B13B56900C84A328DE198B764878F8B06663D5E',
)
# FingerPrint
def stream_handler(message):
  print(message)
  if(message['data'] is 1):
    response = pn_client.publish(
    interests=['hello'],
publish_body={
'apns': {
'aps': {
'alert': 'Hello!',
},
},
'fcm': {
'notification': {
'title': 'Security System',
'body': 'Sidik Jari Terakses',
},
},
},
)

# PIR
def stream_handlerr(message1):
  print(message1)
  if(message1['data'] is 1):
    response1 = pn_client.publish(
    interests=['hello'],
publish_body={
'apns': {
'aps': {
'alert': 'Hello!',
},
},
'fcm': {
'notification': {
'title': 'Security System',
'body': 'Objek Terdeteksi',
},
},
},
)

# SOLENOID
def stream_handlerrr(message2):
  print(message2)
  if(message2['data'] is 1):
    response2 = pn_client.publish(
    interests=['hello'],
publish_body={
'apns': {
'aps': {
'alert': 'Hello!',
},
},
'fcm': {
'notification': {
'title': 'Security System',
'body': 'Solenoid Terbuka',
},
},
},
)



my_stream = db.child("status/statusFingerprint").stream(stream_handler,None)

my_stream1 = db.child("status/statusPIR").stream(stream_handlerr,None)

my_stream2 = db.child("status/statusSolenoid").stream(stream_handlerrr,None)