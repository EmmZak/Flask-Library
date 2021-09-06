from app import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app=app)
#db.init_app(app)