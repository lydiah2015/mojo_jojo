import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    SECRET_KEY=os.getenv("SECRET_KEY",default="super secret key")
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Development(Config):
    pass

class Production(Config):
    pass


config_options={
    "development":Development,
    "production":Production
}
