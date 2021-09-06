from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from models import db, Tag, Livre, Auteur, User

bp = Blueprint('Auteur', __name__, url_prefix="/auteur")

@bp.route("/edit/<int:id>")
@bp.route("/edit/")
def edit(id=None):

    data = {
        'id': id,
        'auteur': Auteur.query.get(id), 
        'tags': Tag.query.all(),
        'auteurs': Auteur.query.all(),
    }
    return render_template('auteur.html', **data)

@bp.route("/remove/<int:id>")
def remove(id):
    Auteur.query.filter_by(id=id).delete()
    db.session.commit()

    return redirect('/')

@bp.route("/submit", methods=['POST'])
def save():
    nom = request.form.get('nom')
    prenom = request.form.get('prenom')

    try:
        id = int(request.form.get('id'))
        a = Auteur.query.get(id)
        a.nom = nom
        a.prenom = prenom
    except:
        a = Auteur(nom, prenom)
        db.session.add(a)
        
    db.session.commit()

    return redirect('/')
"""
@bp.route('/edit/<id>')
@bp.route('/edit')
def show(id=None):
    
    if id is None:
        data = {
            'id': 999,
            'auteur': {'test': 999}
        }
        return render_template('auteur.html', **data)
    
    return render_template('auteur.html')
"""