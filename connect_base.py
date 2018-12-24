import pyrebase

config = {
  "apiKey": "AIzaSyAt3XIUmt20-xaq-i90yWOgKfCIwYbb9_E",
  "authDomain": "volleyex-57efa.firebaseapp.com",
  "databaseURL": "https://volleyex-57efa.firebaseio.com",
  "storageBucket": "volleyex-57efa.appspot.com"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

db = firebase.database()

# db.child("users").push("its not working")
# db.child("users").push("its working")

result = db.child("ashChild").get()

print(result.val())