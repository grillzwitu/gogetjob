import os


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY','secret_key')
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
    # MAIL_SERVER = 'smtp.googlemail.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get('EMAIL_USER')
    # MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
