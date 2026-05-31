import os
from dotenv import load_dotenv
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://root:pass@localhost:3306/learnsmart")
SECRET_KEY = os.getenv("SECRET_KEY", "demo-key")
DB_NAME = os.getenv("DB_NAME", "learnsmart")
