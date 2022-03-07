from decouple import config as cfg

class Config:
    SECRET_KEY = cfg('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = cfg('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = cfg('MAIL_USERNAME')
    MAIL_PASSWORD = cfg('MAIL_PASSWORD')