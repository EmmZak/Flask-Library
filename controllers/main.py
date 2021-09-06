from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from models import db, Tag, Livre, Auteur, User

bp = Blueprint('Main', __name__, url_prefix="/")

@bp.route('/')
def index():

    data = {
        'tags': Tag.query.all(),
        'auteurs': Auteur.query.all(),
        'livres': Livre.query.all(),
    }

    return render_template('home.html', **data)