import os
from urllib.parse import urlparse

# import pyrebase


config_storage = urlparse(os.environ.get("FIREBASE_URL"))

config = {
    'apiKey': config_storage.path[1:],
    'authDomain': config_storage.params,
    'databaseURL': config_storage.query,
    'storageBucket': config_storage.fragment,
}


def create_connect_firebase(user):
    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()
    user = auth.create_user_with_email_and_password(user.email, user.password)
    auth.send_email_verification(user['idToken'])


def log_in_connect_firebase(user):
    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()
    user = auth.sign_in_with_email_and_password(user.email, user.password)


