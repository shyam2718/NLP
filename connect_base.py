



config = {
  "apiKey": "AIzaSyBYBGUvb0vWScsmHxEukoR-WIDsLMaavuY",
  "authDomain": "hticmodule3.firebaseapp.com",
  "databaseURL": "https://hticmodule3.firebaseio.com",
  "storageBucket": "hticmodule3.appspot.com"
}

firebase = pyrebase.initialize_app(config)

#Authenticate
auth = firebase.auth()
db = firebase.database()

def get_meth(data,db):
    db.child("ash").set("its not working")
    return

#Streaming
def stream_handler(message):
    # print(message["event"]) # put
    # print(message["path"]) 
    print(message["data"]) 
    current_data = message["data"]
    get_meth(current_data,db)

my_stream = db.child("ash").stream(stream_handler)
