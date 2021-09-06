from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(20))
    prenom = db.Column(db.String(20))
    login = db.Column(db.String(10))
    password = db.Column(db.String(10))

    def __init__(self, nom, prenom, login, password):
        self.nom = nom
        self.prenom = prenom
        self.login = login
        self.password = password
    
    def __repr__(self):
        return f"[User {self.id, self.login, self.nom}"

class Auteur(db.Model):
    __tablename__ = "auteurs"

    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(20))
    prenom = db.Column(db.String(20))
    #livre_id = db.relationship('Livre', backred="auteur", lazy=True)

    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    
    def __repr__(self):
        return f"[Auteur {self.nom, self.prenom}"

class Livre(db.Model):
    __tablename__ = "livres"

    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(20))
    date = db.Column(db.DateTime)
    auteur_id = db.Column(db.Integer, db.ForeignKey('auteur.id'))
    auteur = db.relationship(
        'Auteur', 
        backref=db.backref('livres', lazy=True)
    )

    def __init__(self, titre):
        self.titre = titre
        self.date = datetime.now()
    
    def __repr__(self):
        return f"[Livre {self.titre, self.date, self.auteur}]"