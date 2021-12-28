import pyrebase
from pusher_push_notifications import PushNotifications

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

def stream_handler(message):
	print(message)
	if(message['data'] is 1):
		response = beams_client.publish(
  			interests=['hello'],
  			publish_body={
  				'apns':{
  					'aps':{
  						'alert': 'Hello!',
						},
					},
    					'fcm': {
      						'notification': {
       						'title': 'Security Sistem',
        					'body': 'Sidik Jari Terakses',
     						 },
    					},
  				},
		)
print(response['publishId'])


my_stream1 = db.child("statusFingerprint").stream(stream_handler,None)
