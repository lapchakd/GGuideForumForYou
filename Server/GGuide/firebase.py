import os
from urllib.parse import urlparse

import pyrebase


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


def upload_files_profilemodel(user, img):
    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()
    user = auth.sign_in_with_email_and_password(user.email, user.password)
    storage = firebase.storage()
    storage.child("profile_images/" + str(img)).put(img, user['idToken'])


def load_to_server_profile_images(user, img):
    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()
    user = auth.sign_in_with_email_and_password(user.email, user.password)
    storage = firebase.storage()
    storage.child("profile_images/" + str(img)).download('Server/profile_images/' + str(img))


def upload_to_server_article_images(articles):
    firebase = pyrebase.initialize_app(config)
    storage = firebase.storage()
    for article in articles:
        img = article.article_image
        storage.child(str(img)).put(img)


def load_to_server_all_articles_images(articles):
    firebase = pyrebase.initialize_app(config)
    storage = firebase.storage()
    for article in articles:
        img = article.article_image
        storage.child(str(img)).download('Server/profile_images/' + str(img))
