import os
from urllib.parse import urlparse

import pyrebase
from django.contrib.auth import get_user_model

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
    firebase_user = auth.create_user_with_email_and_password(user.email, user.password)
    auth.send_email_verification(firebase_user['idToken'])


def log_in_connect_firebase(user):
    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()
    firebase_user = auth.sign_in_with_email_and_password(user.email, user.password)


def upload_files_profilemodel(user, img):
    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()
    firebase_user = auth.sign_in_with_email_and_password(user.email, user.password)
    storage = firebase.storage()
    storage.child("profile_images/" + str(img)).put(img, firebase_user['idToken'])


def load_to_server_profile_images(users):
    firebase = pyrebase.initialize_app(config)
    storage = firebase.storage()
    auth = firebase.auth()
    firebase_user = auth.sign_in_with_email_and_password("admin@gmail.com", os.environ.get("FIREBASE_ADMIN_PASSWORD"))
    users_image_urls = {}
    for user in users:
        img = user.profile.img
        users_image_urls[user.id] = storage \
            .child("profile_images/" + str(img)) \
            .get_url(firebase_user['idToken'])
    return users_image_urls


def upload_to_server_article_image(image, user):
    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()
    firebase_user = auth.sign_in_with_email_and_password(user.email, user.password)
    storage = firebase.storage()
    storage.child('/article_images/' + str(image)).put(image, firebase_user['idToken'])


def load_to_server_all_articles_images(articles):
    firebase = pyrebase.initialize_app(config)
    storage = firebase.storage()
    auth = firebase.auth()
    firebase_user = auth.sign_in_with_email_and_password("admin@gmail.com", os.environ.get("FIREBASE_ADMIN_PASSWORD"))
    articles_image_urls = {}
    for article in articles:
        img = article.article_image
        articles_image_urls[article.id] = storage\
            .child('/'+str(img))\
            .get_url(firebase_user['idToken'])
    return articles_image_urls
