from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from sqlalchemy import desc
from models import db, Tag, Livre, Auteur, User

bp = Blueprint('Main', __name__, url_prefix="/")

def get_prev_next(page, pages):
    if page - 1 <= 0:
        prev = 1
    else:
        prev = page - 1

    if page + 1 > pages:
        next = page
    else:
        next = page + 1
    return prev, next

sort_options = {
    'default': None,
    'asc': Livre.date.asc(),
    'desc': Livre.date.desc()
}

@bp.route('/')
def index(elements=None):
    page = request.args.get('page', 1, type=int)
    elements = request.args.get('elements', 2, type=int)
    sort = request.args.get('sort', 'asc', type=str)

    pages = Livre.query.count() / elements 
    if not pages.is_integer():
        pages = int(pages) + 1

    prev, next = get_prev_next(page, pages)

    livres = Livre.query.order_by(sort_options.get(sort)).paginate(page=page, per_page=elements).items

    data = {
        'elements': elements,
        'sort': sort,
        'page': page,
        'pages': pages,
        'next': next,
        'prev': prev,
        'tags': Tag.query.all(),
        'auteurs': Auteur.query.all(),
        'livres': livres,
    }

    return render_template('home.html', **data)