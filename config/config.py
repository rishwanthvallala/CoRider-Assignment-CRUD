import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGODB_SETTINGS = {
        'host': os.getenv('MONGODB_URI', 'mongodb://mongodb:27017/user_db')
    }
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')