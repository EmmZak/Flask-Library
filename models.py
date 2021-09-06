from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from datetime import datetime
from sqlalchemy import desc
from sqlalchemy.orm import backref

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
    livres = db.relationship(
        'Livre', 
        backref="auteur", 
        lazy=True
    )

    def __init__(self, nom, prenom, id=None):
        self.id = id
        self.nom = nom
        self.prenom = prenom

    def add_livre(self, l):
        self.livres.append(l)

    def __repr__(self):
        return f"[Auteur {self.id, self.nom, self.prenom, self.livres}]"

tag_livre = db.Table(
    'tag_livre',
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True),
    db.Column('livre_id', db.Integer, db.ForeignKey('livres.id'), primary_key=True)
)

class Livre(db.Model):
    __tablename__ = "livres"

    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(20))
    date = db.Column(db.DateTime)
    # 1-n
    auteur_id = db.Column(db.Integer, db.ForeignKey('auteurs.id'), nullable=False)
    # n-n
    tags = db.relationship(
        'Tag', 
        secondary=tag_livre,
        lazy="subquery",
        #backref=db.backref('livres', lazy=True)
    )
    def add_auteur(self, a):
        self.auteur = a
    def add_tag(self, tag):
        self.tags.append(tag)
    
    def __repr__(self):
        return f"\n[Livre {self.id, self.titre, self.date, self.auteur, self.tags}]\n"

class Tag(db.Model):
    __tablename__ = "tags"
    id = db.Column(db.Integer, primary_key=True)
    titre = titre = db.Column(db.String(20))
    
    def __init__(self, titre):
        self.titre=titre
    
    def __repr__(self):
        return f"[Tag {self.id, self.titre}]"