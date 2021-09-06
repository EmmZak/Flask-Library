from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from models import db, Livre, Auteur, Tag

bp = Blueprint('Livre', __name__, url_prefix="/livre")

@bp.route("/edit/<int:id>")
@bp.route("/edit/")
def edit(id=None):

    data = {
        'id': id,
        'livre': Livre.query.get(id), 
        'auteur': Auteur.query.get(id), 
        'tags': Tag.query.all(),
        'auteurs': Auteur.query.all(),
    }
    return render_template('livre.html', **data)

@bp.route("/submit", methods=['POST'])
def save():
    print("request form", request.form)
    titre = request.form.get('titre')
    auteur_id = request.form.get('auteur_id')
    auteur = Auteur.query.get(auteur_id)
    date = request.form.get('date')
    tagIds = request.form.getlist('tagIds')
    tags = [Tag.query.get(tagId) for tagId in tagIds]

    try:
        id = int(request.form.get('id'))
        l = Livre.query.get(id)
        l.titre=titre
        l.auteur=auteur
        l.date=date
        l.tags=tags
    except:
        l = Livre(titre=titre, auteur=auteur, date=date, tags=tags) 
        db.session.add(l)
        
    db.session.commit()

    return redirect('/')

@bp.route("/remove/<int:id>")
def remove(id):
    l = Livre.query.get(id)
    l.tags = []

    db.session.delete(l)
    db.session.commit()

    return redirect('/')