from flask import Flask, render_template
from controllers import user, livre, auteur, tag, main
from flask_sqlalchemy import SQLAlchemy
from models import db
from database import config

app = Flask(__name__)
app.config.from_object('config')

app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_CONNECTION_URI
db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(main.bp, url_prefix='/')
app.register_blueprint(user.bp, url_prefix='/user')
app.register_blueprint(livre.bp, url_prefix='/livre')
app.register_blueprint(auteur.bp, url_prefix='/auteur')
app.register_blueprint(tag.bp, url_prefix='/tag')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
