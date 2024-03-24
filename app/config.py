import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY',"emergency-password-key")
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
