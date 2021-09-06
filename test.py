from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from datetime import datetime
from sqlalchemy import desc
from sqlalchemy.orm import backref

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost:5432/flask_library"
db = SQLAlchemy(app)


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
    livres = db.relationship('Livre', backref="auteur", lazy=True)

    def __init__(self, nom, prenom):
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

db.drop_all()
db.create_all()

a = Auteur("Manu", "Zak")
db.session.add(a)
db.session.commit()

a = Auteur.query.filter_by(nom="Manu").first()
print(a)

tags = [Tag(t) for t in ['Python', 'Love', 'Sound', "Religion", 'Time']]
db.session.add_all(tags)

tags = Tag.query.all()
print(tags)

l1 = Livre(titre="book with tags")
l1.date=datetime.now()
l1.add_tag(tags[0])
l1.add_tag(tags[2])

l1.add_auteur(a)

db.session.add(l1)
db.session.commit()

l1 = Livre(titre="book with nothing")
l1.date=datetime.now()
l1.add_tag(tags[2])

l1.add_auteur(a)

db.session.add(l1)
db.session.commit()

l = Livre.query.filter_by(id=1).first()
print("l.id=1", l)
"""
l1 = Livre(titre="book with tags")
l1.date=datetime.now()

t = Tag('Python')
l1.add_tag(t)
t = Tag('Music')
l1.add_tag(t)
t = Tag('Love')
l1.add_tag(t)
"""

#l1.add_auteur(a)

#print(l1)
"""
l1 = Livre(titre="book with tags")
l1.date=datetime.now()
l2 = Livre(titre="book_99")
l2.date=datetime.now()

a1 = Auteur(nom="Ero", prenom="Zak")
a1.livres.append(l1)
a1.livres.append(l2)

db.session.add(a1)

db.session.commit()

db.create_all()
a2 = Auteur(nom="Miko", prenom="Zak")

l1 = Livre(titre="final", auteur=a2)
l1.date=datetime.now()

db.session.add(a2)
db.session.commit()
"""