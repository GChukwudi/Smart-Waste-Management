import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '1c19601034ac56d15b52f9a21c3f3538e016db97d3ba76da2685fa7e668d1dc0'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql+pymysql://adminuser:mypassword@localhost/smart_waste_management'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
