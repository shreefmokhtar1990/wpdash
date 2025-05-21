
import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'jwt_secret')
    CELERY_BROKER_URL = os.getenv('REDIS_URL')
    CELERY_RESULT_BACKEND = os.getenv('REDIS_URL')
