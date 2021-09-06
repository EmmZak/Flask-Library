from flask import Flask, render_template
from controllers import user, livre, auteur, tag, main
from flask_sqlalchemy import SQLAlchemy
from models import db

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)

app.register_blueprint(main.bp, url_prefix='/')
app.register_blueprint(user.bp, url_prefix='/user')
app.register_blueprint(livre.bp, url_prefix='/livre')
app.register_blueprint(auteur.bp, url_prefix='/auteur')
app.register_blueprint(tag.bp, url_prefix='/tag')


if __name__ == '__main__':
    app.debug = True    
    app.run()
